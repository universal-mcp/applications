# Extend __path__ to enable namespace package behavior
# This allows universal_mcp.applications to be discovered from multiple packages
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
