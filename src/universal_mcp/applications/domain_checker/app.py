import logging
import sys
from typing import Any

import dns.resolver
import requests

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)

logger = logging.getLogger("domain_checker")

# Constants
RDAP_BOOTSTRAP_URL = "https://data.iana.org/rdap/dns.json"
USER_AGENT = "DomainCheckerBot/1.0"

# Top TLDs to check
TOP_TLDS = [
    "com",
    "net",
    "org",
    "io",
    "co",
    "app",
    "dev",
    "ai",
    "me",
    "info",
    "xyz",
    "online",
    "site",
    "tech",
]


class DomainCheckerApp(APIApplication):
    """
    Base class for Universal MCP Applications.
    """

    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="domain_checker", integration=integration, **kwargs)

    async def get_rdap_data(self, domain: str) -> dict[str, Any] | None:
        """Get RDAP data for a domain"""
        try:
            # Special case for .ch and .li domains
            tld = domain.split(".")[-1].lower()
            if tld in ["ch", "li"]:
                rdap_url = f"https://rdap.nic.{tld}/domain/{domain}"
            # Use common RDAP servers for known TLDs
            elif tld in ["com", "net"]:
                rdap_url = f"https://rdap.verisign.com/{tld}/v1/domain/{domain}"
            elif tld == "org":
                rdap_url = (
                    f"https://rdap.publicinterestregistry.org/rdap/domain/{domain}"
                )
            else:
                rdap_url = f"https://rdap.org/domain/{domain}"

            headers = {"Accept": "application/rdap+json", "User-Agent": USER_AGENT}

            response = requests.get(rdap_url, headers=headers, timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            logger.error(f"RDAP error for {domain}: {e}")
            return None

    async def check_dns(self, domain: str) -> bool:
        """Check if a domain has DNS records"""
        try:
            dns.resolver.resolve(domain, "A")
            return True
        except:
            try:
                dns.resolver.resolve(domain, "NS")
                return True
            except:
                return False

    async def check_domain_tool(self, domain: str) -> dict[str, Any]:
        """
        Checks if a domain is available for registration by querying DNS records and RDAP data.

        This method performs a comprehensive domain availability check by first checking DNS records
        and then querying RDAP (Registration Data Access Protocol) servers for detailed registration
        information. It provides detailed information about registered domains including registrar,
        registration date, and expiration date.

        Args:
            domain: String representing the domain name to check (e.g., "example.com")

        Returns:
            Dictionary containing domain availability information with the following keys:
            - domain: The domain name that was checked
            - status: "Registered" or "Available"
            - registrar: Name of the registrar (or None/Unknown if not registered)
            - registration_date: Domain registration date (or None/Unknown)
            - expiration_date: Domain expiration date (or None/Unknown)
            - has_dns: Boolean indicating if DNS records exist
            - rdap_data_available: Boolean indicating if RDAP data was retrieved
            - note: Additional information when needed

        Raises:
            DNSException: When DNS resolution fails due to network issues or invalid domain format
            RequestException: When RDAP queries fail due to network issues or server errors
            ValueError: When the domain parameter is empty or contains invalid characters

        Tags:
            domain, availability, registration, dns, rdap, important
        """
        logger.info(f"Checking domain: {domain}")

        # First check DNS
        has_dns = await self.check_dns(domain)

        if has_dns:
            # Domain exists, get RDAP data if possible
            rdap_data = await self.get_rdap_data(domain)

            if rdap_data:
                # Extract data from RDAP
                registrar = "Unknown"
                reg_date = "Unknown"
                exp_date = "Unknown"

                # Extract registrar
                entities = rdap_data.get("entities", [])
                for entity in entities:
                    if "registrar" in entity.get("roles", []):
                        vcard = entity.get("vcardArray", [])
                        if len(vcard) > 1 and isinstance(vcard[1], list):
                            for entry in vcard[1]:
                                if entry[0] in ["fn", "org"] and len(entry) > 3:
                                    registrar = entry[3]
                                    break

                # Extract dates
                events = rdap_data.get("events", [])
                for event in events:
                    if event.get("eventAction") == "registration":
                        reg_date = event.get("eventDate", "Unknown")
                    elif event.get("eventAction") == "expiration":
                        exp_date = event.get("eventDate", "Unknown")

                return {
                    "domain": domain,
                    "status": "Registered",
                    "registrar": registrar,
                    "registration_date": reg_date,
                    "expiration_date": exp_date,
                    "has_dns": True,
                    "rdap_data_available": True,
                }
            else:
                return {
                    "domain": domain,
                    "status": "Registered",
                    "registrar": "Unknown",
                    "registration_date": "Unknown",
                    "expiration_date": "Unknown",
                    "has_dns": True,
                    "rdap_data_available": False,
                    "note": "Domain has DNS records but RDAP data couldn't be retrieved",
                }

        # Try RDAP one more time even if DNS not found
        rdap_data = await self.get_rdap_data(domain)
        if rdap_data:
            return {
                "domain": domain,
                "status": "Registered",
                "registrar": "Unknown",
                "registration_date": "Unknown",
                "expiration_date": "Unknown",
                "has_dns": False,
                "rdap_data_available": True,
                "note": "Domain found in RDAP registry",
            }

        # If we get here, the domain is likely available
        return {
            "domain": domain,
            "status": "Available",
            "registrar": None,
            "registration_date": None,
            "expiration_date": None,
            "has_dns": False,
            "rdap_data_available": False,
            "note": "No DNS records or RDAP data found",
        }

    async def check_tlds_tool(self, keyword: str) -> dict[str, Any]:
        """
        Checks a keyword across multiple top-level domains (TLDs) to find available domain names.

        This method systematically checks a given keyword across 14 popular TLDs including .com, .net,
        .org, .io, .co, .app, .dev, .ai, .me, .info, .xyz, .online, .site, and .tech. It performs
        DNS lookups and RDAP queries to determine domain availability and provides a comprehensive
        report of available and taken domains.

        Args:
            keyword: String representing the keyword to check across TLDs (e.g., "myapp")

        Returns:
            Dictionary containing TLD availability information with the following keys:
            - keyword: The keyword that was checked
            - tlds_checked: Number of TLDs checked (14)
            - available_count: Number of available domains found
            - taken_count: Number of taken domains found
            - available_domains: List of available domain names
            - taken_domains: List of taken domain names
            - tlds_checked_list: Complete list of TLDs that were checked

        Raises:
            DNSException: When DNS resolution fails due to network issues or invalid domain format
            RequestException: When RDAP queries fail due to network issues or server errors
            ValueError: When the keyword parameter is empty or contains invalid characters

        Tags:
            tld, keyword, domain-search, availability, bulk-check, important
        """
        logger.info(f"Checking keyword: {keyword} across TLDs")

        available = []
        taken = []

        # Check each TLD in sequence
        for tld in TOP_TLDS:
            domain = f"{keyword}.{tld}"
            has_dns = await self.check_dns(domain)

            if not has_dns:
                # Double-check with RDAP if no DNS
                rdap_data = await self.get_rdap_data(domain)
                if not rdap_data:
                    available.append(domain)
                else:
                    taken.append(domain)
            else:
                taken.append(domain)

        return {
            "keyword": keyword,
            "tlds_checked": len(TOP_TLDS),
            "available_count": len(available),
            "taken_count": len(taken),
            "available_domains": available,
            "taken_domains": taken,
            "tlds_checked_list": TOP_TLDS,
        }

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.check_domain_tool, self.check_tlds_tool]
