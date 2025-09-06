from typing import Any

from universal_mcp.applications.application import APIApplication
from universal_mcp.integrations import Integration


class PosthogApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="posthog", integration=integration, **kwargs)
        self.base_url = "https://us.posthog.com"

    def is_generating_demo_data_retrieve(self, organization_id, id) -> dict[str, Any]:
        """
        Checks if demo data is being generated for a specific project within an organization.

        Args:
            organization_id (string): organization_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, projects
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/projects/{id}/is_generating_demo_data/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def reset_token_partial_update(
        self,
        organization_id,
        id,
        id_body=None,
        organization=None,
        name=None,
        product_description=None,
        created_at=None,
        effective_membership_level=None,
        has_group_types=None,
        group_types=None,
        live_events_token=None,
        updated_at=None,
        uuid=None,
        api_token=None,
        app_urls=None,
        slack_incoming_webhook=None,
        anonymize_ips=None,
        completed_snippet_onboarding=None,
        ingested_event=None,
        test_account_filters=None,
        test_account_filters_default_checked=None,
        path_cleaning_filters=None,
        is_demo=None,
        timezone=None,
        data_attributes=None,
        person_display_name_properties=None,
        correlation_config=None,
        autocapture_opt_out=None,
        autocapture_exceptions_opt_in=None,
        autocapture_web_vitals_opt_in=None,
        autocapture_web_vitals_allowed_metrics=None,
        autocapture_exceptions_errors_to_ignore=None,
        capture_console_log_opt_in=None,
        capture_performance_opt_in=None,
        session_recording_opt_in=None,
        session_recording_sample_rate=None,
        session_recording_minimum_duration_milliseconds=None,
        session_recording_linked_flag=None,
        session_recording_network_payload_capture_config=None,
        session_recording_masking_config=None,
        session_replay_config=None,
        survey_config=None,
        access_control=None,
        week_start_day=None,
        primary_dashboard=None,
        live_events_columns=None,
        recording_domains=None,
        person_on_events_querying_enabled=None,
        inject_web_apps=None,
        extra_settings=None,
        modifiers=None,
        default_modifiers=None,
        has_completed_onboarding_for=None,
        surveys_opt_in=None,
        heatmaps_opt_in=None,
        product_intents=None,
        flags_persistence_default=None,
    ) -> dict[str, Any]:
        """
        Resets the authentication token for a specific project within an organization and returns a success status.

        Args:
            organization_id (string): organization_id
            id (string): id
            id_body (integer): id
            organization (string): organization
            name (string): name
            product_description (string): product_description
            created_at (string): created_at
            effective_membership_level (string): effective_membership_level
            has_group_types (boolean): has_group_types
            group_types (array): group_types
            live_events_token (string): live_events_token
            updated_at (string): updated_at
            uuid (string): uuid
            api_token (string): api_token
            app_urls (array): app_urls
            slack_incoming_webhook (string): slack_incoming_webhook
            anonymize_ips (boolean): anonymize_ips
            completed_snippet_onboarding (boolean): completed_snippet_onboarding
            ingested_event (boolean): ingested_event
            test_account_filters (string): test_account_filters
            test_account_filters_default_checked (boolean): test_account_filters_default_checked
            path_cleaning_filters (string): path_cleaning_filters
            is_demo (boolean): is_demo
            timezone (string): * `Africa/Abidjan` - Africa/Abidjan
        * `Africa/Accra` - Africa/Accra
        * `Africa/Addis_Ababa` - Africa/Addis_Ababa
        * `Africa/Algiers` - Africa/Algiers
        * `Africa/Asmara` - Africa/Asmara
        * `Africa/Asmera` - Africa/Asmera
        * `Africa/Bamako` - Africa/Bamako
        * `Africa/Bangui` - Africa/Bangui
        * `Africa/Banjul` - Africa/Banjul
        * `Africa/Bissau` - Africa/Bissau
        * `Africa/Blantyre` - Africa/Blantyre
        * `Africa/Brazzaville` - Africa/Brazzaville
        * `Africa/Bujumbura` - Africa/Bujumbura
        * `Africa/Cairo` - Africa/Cairo
        * `Africa/Casablanca` - Africa/Casablanca
        * `Africa/Ceuta` - Africa/Ceuta
        * `Africa/Conakry` - Africa/Conakry
        * `Africa/Dakar` - Africa/Dakar
        * `Africa/Dar_es_Salaam` - Africa/Dar_es_Salaam
        * `Africa/Djibouti` - Africa/Djibouti
        * `Africa/Douala` - Africa/Douala
        * `Africa/El_Aaiun` - Africa/El_Aaiun
        * `Africa/Freetown` - Africa/Freetown
        * `Africa/Gaborone` - Africa/Gaborone
        * `Africa/Harare` - Africa/Harare
        * `Africa/Johannesburg` - Africa/Johannesburg
        * `Africa/Juba` - Africa/Juba
        * `Africa/Kampala` - Africa/Kampala
        * `Africa/Khartoum` - Africa/Khartoum
        * `Africa/Kigali` - Africa/Kigali
        * `Africa/Kinshasa` - Africa/Kinshasa
        * `Africa/Lagos` - Africa/Lagos
        * `Africa/Libreville` - Africa/Libreville
        * `Africa/Lome` - Africa/Lome
        * `Africa/Luanda` - Africa/Luanda
        * `Africa/Lubumbashi` - Africa/Lubumbashi
        * `Africa/Lusaka` - Africa/Lusaka
        * `Africa/Malabo` - Africa/Malabo
        * `Africa/Maputo` - Africa/Maputo
        * `Africa/Maseru` - Africa/Maseru
        * `Africa/Mbabane` - Africa/Mbabane
        * `Africa/Mogadishu` - Africa/Mogadishu
        * `Africa/Monrovia` - Africa/Monrovia
        * `Africa/Nairobi` - Africa/Nairobi
        * `Africa/Ndjamena` - Africa/Ndjamena
        * `Africa/Niamey` - Africa/Niamey
        * `Africa/Nouakchott` - Africa/Nouakchott
        * `Africa/Ouagadougou` - Africa/Ouagadougou
        * `Africa/Porto-Novo` - Africa/Porto-Novo
        * `Africa/Sao_Tome` - Africa/Sao_Tome
        * `Africa/Timbuktu` - Africa/Timbuktu
        * `Africa/Tripoli` - Africa/Tripoli
        * `Africa/Tunis` - Africa/Tunis
        * `Africa/Windhoek` - Africa/Windhoek
        * `America/Adak` - America/Adak
        * `America/Anchorage` - America/Anchorage
        * `America/Anguilla` - America/Anguilla
        * `America/Antigua` - America/Antigua
        * `America/Araguaina` - America/Araguaina
        * `America/Argentina/Buenos_Aires` - America/Argentina/Buenos_Aires
        * `America/Argentina/Catamarca` - America/Argentina/Catamarca
        * `America/Argentina/ComodRivadavia` - America/Argentina/ComodRivadavia
        * `America/Argentina/Cordoba` - America/Argentina/Cordoba
        * `America/Argentina/Jujuy` - America/Argentina/Jujuy
        * `America/Argentina/La_Rioja` - America/Argentina/La_Rioja
        * `America/Argentina/Mendoza` - America/Argentina/Mendoza
        * `America/Argentina/Rio_Gallegos` - America/Argentina/Rio_Gallegos
        * `America/Argentina/Salta` - America/Argentina/Salta
        * `America/Argentina/San_Juan` - America/Argentina/San_Juan
        * `America/Argentina/San_Luis` - America/Argentina/San_Luis
        * `America/Argentina/Tucuman` - America/Argentina/Tucuman
        * `America/Argentina/Ushuaia` - America/Argentina/Ushuaia
        * `America/Aruba` - America/Aruba
        * `America/Asuncion` - America/Asuncion
        * `America/Atikokan` - America/Atikokan
        * `America/Atka` - America/Atka
        * `America/Bahia` - America/Bahia
        * `America/Bahia_Banderas` - America/Bahia_Banderas
        * `America/Barbados` - America/Barbados
        * `America/Belem` - America/Belem
        * `America/Belize` - America/Belize
        * `America/Blanc-Sablon` - America/Blanc-Sablon
        * `America/Boa_Vista` - America/Boa_Vista
        * `America/Bogota` - America/Bogota
        * `America/Boise` - America/Boise
        * `America/Buenos_Aires` - America/Buenos_Aires
        * `America/Cambridge_Bay` - America/Cambridge_Bay
        * `America/Campo_Grande` - America/Campo_Grande
        * `America/Cancun` - America/Cancun
        * `America/Caracas` - America/Caracas
        * `America/Catamarca` - America/Catamarca
        * `America/Cayenne` - America/Cayenne
        * `America/Cayman` - America/Cayman
        * `America/Chicago` - America/Chicago
        * `America/Chihuahua` - America/Chihuahua
        * `America/Ciudad_Juarez` - America/Ciudad_Juarez
        * `America/Coral_Harbour` - America/Coral_Harbour
        * `America/Cordoba` - America/Cordoba
        * `America/Costa_Rica` - America/Costa_Rica
        * `America/Creston` - America/Creston
        * `America/Cuiaba` - America/Cuiaba
        * `America/Curacao` - America/Curacao
        * `America/Danmarkshavn` - America/Danmarkshavn
        * `America/Dawson` - America/Dawson
        * `America/Dawson_Creek` - America/Dawson_Creek
        * `America/Denver` - America/Denver
        * `America/Detroit` - America/Detroit
        * `America/Dominica` - America/Dominica
        * `America/Edmonton` - America/Edmonton
        * `America/Eirunepe` - America/Eirunepe
        * `America/El_Salvador` - America/El_Salvador
        * `America/Ensenada` - America/Ensenada
        * `America/Fort_Nelson` - America/Fort_Nelson
        * `America/Fort_Wayne` - America/Fort_Wayne
        * `America/Fortaleza` - America/Fortaleza
        * `America/Glace_Bay` - America/Glace_Bay
        * `America/Godthab` - America/Godthab
        * `America/Goose_Bay` - America/Goose_Bay
        * `America/Grand_Turk` - America/Grand_Turk
        * `America/Grenada` - America/Grenada
        * `America/Guadeloupe` - America/Guadeloupe
        * `America/Guatemala` - America/Guatemala
        * `America/Guayaquil` - America/Guayaquil
        * `America/Guyana` - America/Guyana
        * `America/Halifax` - America/Halifax
        * `America/Havana` - America/Havana
        * `America/Hermosillo` - America/Hermosillo
        * `America/Indiana/Indianapolis` - America/Indiana/Indianapolis
        * `America/Indiana/Knox` - America/Indiana/Knox
        * `America/Indiana/Marengo` - America/Indiana/Marengo
        * `America/Indiana/Petersburg` - America/Indiana/Petersburg
        * `America/Indiana/Tell_City` - America/Indiana/Tell_City
        * `America/Indiana/Vevay` - America/Indiana/Vevay
        * `America/Indiana/Vincennes` - America/Indiana/Vincennes
        * `America/Indiana/Winamac` - America/Indiana/Winamac
        * `America/Indianapolis` - America/Indianapolis
        * `America/Inuvik` - America/Inuvik
        * `America/Iqaluit` - America/Iqaluit
        * `America/Jamaica` - America/Jamaica
        * `America/Jujuy` - America/Jujuy
        * `America/Juneau` - America/Juneau
        * `America/Kentucky/Louisville` - America/Kentucky/Louisville
        * `America/Kentucky/Monticello` - America/Kentucky/Monticello
        * `America/Knox_IN` - America/Knox_IN
        * `America/Kralendijk` - America/Kralendijk
        * `America/La_Paz` - America/La_Paz
        * `America/Lima` - America/Lima
        * `America/Los_Angeles` - America/Los_Angeles
        * `America/Louisville` - America/Louisville
        * `America/Lower_Princes` - America/Lower_Princes
        * `America/Maceio` - America/Maceio
        * `America/Managua` - America/Managua
        * `America/Manaus` - America/Manaus
        * `America/Marigot` - America/Marigot
        * `America/Martinique` - America/Martinique
        * `America/Matamoros` - America/Matamoros
        * `America/Mazatlan` - America/Mazatlan
        * `America/Mendoza` - America/Mendoza
        * `America/Menominee` - America/Menominee
        * `America/Merida` - America/Merida
        * `America/Metlakatla` - America/Metlakatla
        * `America/Mexico_City` - America/Mexico_City
        * `America/Miquelon` - America/Miquelon
        * `America/Moncton` - America/Moncton
        * `America/Monterrey` - America/Monterrey
        * `America/Montevideo` - America/Montevideo
        * `America/Montreal` - America/Montreal
        * `America/Montserrat` - America/Montserrat
        * `America/Nassau` - America/Nassau
        * `America/New_York` - America/New_York
        * `America/Nipigon` - America/Nipigon
        * `America/Nome` - America/Nome
        * `America/Noronha` - America/Noronha
        * `America/North_Dakota/Beulah` - America/North_Dakota/Beulah
        * `America/North_Dakota/Center` - America/North_Dakota/Center
        * `America/North_Dakota/New_Salem` - America/North_Dakota/New_Salem
        * `America/Nuuk` - America/Nuuk
        * `America/Ojinaga` - America/Ojinaga
        * `America/Panama` - America/Panama
        * `America/Pangnirtung` - America/Pangnirtung
        * `America/Paramaribo` - America/Paramaribo
        * `America/Phoenix` - America/Phoenix
        * `America/Port-au-Prince` - America/Port-au-Prince
        * `America/Port_of_Spain` - America/Port_of_Spain
        * `America/Porto_Acre` - America/Porto_Acre
        * `America/Porto_Velho` - America/Porto_Velho
        * `America/Puerto_Rico` - America/Puerto_Rico
        * `America/Punta_Arenas` - America/Punta_Arenas
        * `America/Rainy_River` - America/Rainy_River
        * `America/Rankin_Inlet` - America/Rankin_Inlet
        * `America/Recife` - America/Recife
        * `America/Regina` - America/Regina
        * `America/Resolute` - America/Resolute
        * `America/Rio_Branco` - America/Rio_Branco
        * `America/Rosario` - America/Rosario
        * `America/Santa_Isabel` - America/Santa_Isabel
        * `America/Santarem` - America/Santarem
        * `America/Santiago` - America/Santiago
        * `America/Santo_Domingo` - America/Santo_Domingo
        * `America/Sao_Paulo` - America/Sao_Paulo
        * `America/Scoresbysund` - America/Scoresbysund
        * `America/Shiprock` - America/Shiprock
        * `America/Sitka` - America/Sitka
        * `America/St_Barthelemy` - America/St_Barthelemy
        * `America/St_Johns` - America/St_Johns
        * `America/St_Kitts` - America/St_Kitts
        * `America/St_Lucia` - America/St_Lucia
        * `America/St_Thomas` - America/St_Thomas
        * `America/St_Vincent` - America/St_Vincent
        * `America/Swift_Current` - America/Swift_Current
        * `America/Tegucigalpa` - America/Tegucigalpa
        * `America/Thule` - America/Thule
        * `America/Thunder_Bay` - America/Thunder_Bay
        * `America/Tijuana` - America/Tijuana
        * `America/Toronto` - America/Toronto
        * `America/Tortola` - America/Tortola
        * `America/Vancouver` - America/Vancouver
        * `America/Virgin` - America/Virgin
        * `America/Whitehorse` - America/Whitehorse
        * `America/Winnipeg` - America/Winnipeg
        * `America/Yakutat` - America/Yakutat
        * `America/Yellowknife` - America/Yellowknife
        * `Antarctica/Casey` - Antarctica/Casey
        * `Antarctica/Davis` - Antarctica/Davis
        * `Antarctica/DumontDUrville` - Antarctica/DumontDUrville
        * `Antarctica/Macquarie` - Antarctica/Macquarie
        * `Antarctica/Mawson` - Antarctica/Mawson
        * `Antarctica/McMurdo` - Antarctica/McMurdo
        * `Antarctica/Palmer` - Antarctica/Palmer
        * `Antarctica/Rothera` - Antarctica/Rothera
        * `Antarctica/South_Pole` - Antarctica/South_Pole
        * `Antarctica/Syowa` - Antarctica/Syowa
        * `Antarctica/Troll` - Antarctica/Troll
        * `Antarctica/Vostok` - Antarctica/Vostok
        * `Arctic/Longyearbyen` - Arctic/Longyearbyen
        * `Asia/Aden` - Asia/Aden
        * `Asia/Almaty` - Asia/Almaty
        * `Asia/Amman` - Asia/Amman
        * `Asia/Anadyr` - Asia/Anadyr
        * `Asia/Aqtau` - Asia/Aqtau
        * `Asia/Aqtobe` - Asia/Aqtobe
        * `Asia/Ashgabat` - Asia/Ashgabat
        * `Asia/Ashkhabad` - Asia/Ashkhabad
        * `Asia/Atyrau` - Asia/Atyrau
        * `Asia/Baghdad` - Asia/Baghdad
        * `Asia/Bahrain` - Asia/Bahrain
        * `Asia/Baku` - Asia/Baku
        * `Asia/Bangkok` - Asia/Bangkok
        * `Asia/Barnaul` - Asia/Barnaul
        * `Asia/Beirut` - Asia/Beirut
        * `Asia/Bishkek` - Asia/Bishkek
        * `Asia/Brunei` - Asia/Brunei
        * `Asia/Calcutta` - Asia/Calcutta
        * `Asia/Chita` - Asia/Chita
        * `Asia/Choibalsan` - Asia/Choibalsan
        * `Asia/Chongqing` - Asia/Chongqing
        * `Asia/Chungking` - Asia/Chungking
        * `Asia/Colombo` - Asia/Colombo
        * `Asia/Dacca` - Asia/Dacca
        * `Asia/Damascus` - Asia/Damascus
        * `Asia/Dhaka` - Asia/Dhaka
        * `Asia/Dili` - Asia/Dili
        * `Asia/Dubai` - Asia/Dubai
        * `Asia/Dushanbe` - Asia/Dushanbe
        * `Asia/Famagusta` - Asia/Famagusta
        * `Asia/Gaza` - Asia/Gaza
        * `Asia/Harbin` - Asia/Harbin
        * `Asia/Hebron` - Asia/Hebron
        * `Asia/Ho_Chi_Minh` - Asia/Ho_Chi_Minh
        * `Asia/Hong_Kong` - Asia/Hong_Kong
        * `Asia/Hovd` - Asia/Hovd
        * `Asia/Irkutsk` - Asia/Irkutsk
        * `Asia/Istanbul` - Asia/Istanbul
        * `Asia/Jakarta` - Asia/Jakarta
        * `Asia/Jayapura` - Asia/Jayapura
        * `Asia/Jerusalem` - Asia/Jerusalem
        * `Asia/Kabul` - Asia/Kabul
        * `Asia/Kamchatka` - Asia/Kamchatka
        * `Asia/Karachi` - Asia/Karachi
        * `Asia/Kashgar` - Asia/Kashgar
        * `Asia/Kathmandu` - Asia/Kathmandu
        * `Asia/Katmandu` - Asia/Katmandu
        * `Asia/Khandyga` - Asia/Khandyga
        * `Asia/Kolkata` - Asia/Kolkata
        * `Asia/Krasnoyarsk` - Asia/Krasnoyarsk
        * `Asia/Kuala_Lumpur` - Asia/Kuala_Lumpur
        * `Asia/Kuching` - Asia/Kuching
        * `Asia/Kuwait` - Asia/Kuwait
        * `Asia/Macao` - Asia/Macao
        * `Asia/Macau` - Asia/Macau
        * `Asia/Magadan` - Asia/Magadan
        * `Asia/Makassar` - Asia/Makassar
        * `Asia/Manila` - Asia/Manila
        * `Asia/Muscat` - Asia/Muscat
        * `Asia/Nicosia` - Asia/Nicosia
        * `Asia/Novokuznetsk` - Asia/Novokuznetsk
        * `Asia/Novosibirsk` - Asia/Novosibirsk
        * `Asia/Omsk` - Asia/Omsk
        * `Asia/Oral` - Asia/Oral
        * `Asia/Phnom_Penh` - Asia/Phnom_Penh
        * `Asia/Pontianak` - Asia/Pontianak
        * `Asia/Pyongyang` - Asia/Pyongyang
        * `Asia/Qatar` - Asia/Qatar
        * `Asia/Qostanay` - Asia/Qostanay
        * `Asia/Qyzylorda` - Asia/Qyzylorda
        * `Asia/Rangoon` - Asia/Rangoon
        * `Asia/Riyadh` - Asia/Riyadh
        * `Asia/Saigon` - Asia/Saigon
        * `Asia/Sakhalin` - Asia/Sakhalin
        * `Asia/Samarkand` - Asia/Samarkand
        * `Asia/Seoul` - Asia/Seoul
        * `Asia/Shanghai` - Asia/Shanghai
        * `Asia/Singapore` - Asia/Singapore
        * `Asia/Srednekolymsk` - Asia/Srednekolymsk
        * `Asia/Taipei` - Asia/Taipei
        * `Asia/Tashkent` - Asia/Tashkent
        * `Asia/Tbilisi` - Asia/Tbilisi
        * `Asia/Tehran` - Asia/Tehran
        * `Asia/Tel_Aviv` - Asia/Tel_Aviv
        * `Asia/Thimbu` - Asia/Thimbu
        * `Asia/Thimphu` - Asia/Thimphu
        * `Asia/Tokyo` - Asia/Tokyo
        * `Asia/Tomsk` - Asia/Tomsk
        * `Asia/Ujung_Pandang` - Asia/Ujung_Pandang
        * `Asia/Ulaanbaatar` - Asia/Ulaanbaatar
        * `Asia/Ulan_Bator` - Asia/Ulan_Bator
        * `Asia/Urumqi` - Asia/Urumqi
        * `Asia/Ust-Nera` - Asia/Ust-Nera
        * `Asia/Vientiane` - Asia/Vientiane
        * `Asia/Vladivostok` - Asia/Vladivostok
        * `Asia/Yakutsk` - Asia/Yakutsk
        * `Asia/Yangon` - Asia/Yangon
        * `Asia/Yekaterinburg` - Asia/Yekaterinburg
        * `Asia/Yerevan` - Asia/Yerevan
        * `Atlantic/Azores` - Atlantic/Azores
        * `Atlantic/Bermuda` - Atlantic/Bermuda
        * `Atlantic/Canary` - Atlantic/Canary
        * `Atlantic/Cape_Verde` - Atlantic/Cape_Verde
        * `Atlantic/Faeroe` - Atlantic/Faeroe
        * `Atlantic/Faroe` - Atlantic/Faroe
        * `Atlantic/Jan_Mayen` - Atlantic/Jan_Mayen
        * `Atlantic/Madeira` - Atlantic/Madeira
        * `Atlantic/Reykjavik` - Atlantic/Reykjavik
        * `Atlantic/South_Georgia` - Atlantic/South_Georgia
        * `Atlantic/St_Helena` - Atlantic/St_Helena
        * `Atlantic/Stanley` - Atlantic/Stanley
        * `Australia/ACT` - Australia/ACT
        * `Australia/Adelaide` - Australia/Adelaide
        * `Australia/Brisbane` - Australia/Brisbane
        * `Australia/Broken_Hill` - Australia/Broken_Hill
        * `Australia/Canberra` - Australia/Canberra
        * `Australia/Currie` - Australia/Currie
        * `Australia/Darwin` - Australia/Darwin
        * `Australia/Eucla` - Australia/Eucla
        * `Australia/Hobart` - Australia/Hobart
        * `Australia/LHI` - Australia/LHI
        * `Australia/Lindeman` - Australia/Lindeman
        * `Australia/Lord_Howe` - Australia/Lord_Howe
        * `Australia/Melbourne` - Australia/Melbourne
        * `Australia/NSW` - Australia/NSW
        * `Australia/North` - Australia/North
        * `Australia/Perth` - Australia/Perth
        * `Australia/Queensland` - Australia/Queensland
        * `Australia/South` - Australia/South
        * `Australia/Sydney` - Australia/Sydney
        * `Australia/Tasmania` - Australia/Tasmania
        * `Australia/Victoria` - Australia/Victoria
        * `Australia/West` - Australia/West
        * `Australia/Yancowinna` - Australia/Yancowinna
        * `Brazil/Acre` - Brazil/Acre
        * `Brazil/DeNoronha` - Brazil/DeNoronha
        * `Brazil/East` - Brazil/East
        * `Brazil/West` - Brazil/West
        * `CET` - CET
        * `CST6CDT` - CST6CDT
        * `Canada/Atlantic` - Canada/Atlantic
        * `Canada/Central` - Canada/Central
        * `Canada/Eastern` - Canada/Eastern
        * `Canada/Mountain` - Canada/Mountain
        * `Canada/Newfoundland` - Canada/Newfoundland
        * `Canada/Pacific` - Canada/Pacific
        * `Canada/Saskatchewan` - Canada/Saskatchewan
        * `Canada/Yukon` - Canada/Yukon
        * `Chile/Continental` - Chile/Continental
        * `Chile/EasterIsland` - Chile/EasterIsland
        * `Cuba` - Cuba
        * `EET` - EET
        * `EST` - EST
        * `EST5EDT` - EST5EDT
        * `Egypt` - Egypt
        * `Eire` - Eire
        * `Etc/GMT` - Etc/GMT
        * `Etc/GMT+0` - Etc/GMT+0
        * `Etc/GMT+1` - Etc/GMT+1
        * `Etc/GMT+10` - Etc/GMT+10
        * `Etc/GMT+11` - Etc/GMT+11
        * `Etc/GMT+12` - Etc/GMT+12
        * `Etc/GMT+2` - Etc/GMT+2
        * `Etc/GMT+3` - Etc/GMT+3
        * `Etc/GMT+4` - Etc/GMT+4
        * `Etc/GMT+5` - Etc/GMT+5
        * `Etc/GMT+6` - Etc/GMT+6
        * `Etc/GMT+7` - Etc/GMT+7
        * `Etc/GMT+8` - Etc/GMT+8
        * `Etc/GMT+9` - Etc/GMT+9
        * `Etc/GMT-0` - Etc/GMT-0
        * `Etc/GMT-1` - Etc/GMT-1
        * `Etc/GMT-10` - Etc/GMT-10
        * `Etc/GMT-11` - Etc/GMT-11
        * `Etc/GMT-12` - Etc/GMT-12
        * `Etc/GMT-13` - Etc/GMT-13
        * `Etc/GMT-14` - Etc/GMT-14
        * `Etc/GMT-2` - Etc/GMT-2
        * `Etc/GMT-3` - Etc/GMT-3
        * `Etc/GMT-4` - Etc/GMT-4
        * `Etc/GMT-5` - Etc/GMT-5
        * `Etc/GMT-6` - Etc/GMT-6
        * `Etc/GMT-7` - Etc/GMT-7
        * `Etc/GMT-8` - Etc/GMT-8
        * `Etc/GMT-9` - Etc/GMT-9
        * `Etc/GMT0` - Etc/GMT0
        * `Etc/Greenwich` - Etc/Greenwich
        * `Etc/UCT` - Etc/UCT
        * `Etc/UTC` - Etc/UTC
        * `Etc/Universal` - Etc/Universal
        * `Etc/Zulu` - Etc/Zulu
        * `Europe/Amsterdam` - Europe/Amsterdam
        * `Europe/Andorra` - Europe/Andorra
        * `Europe/Astrakhan` - Europe/Astrakhan
        * `Europe/Athens` - Europe/Athens
        * `Europe/Belfast` - Europe/Belfast
        * `Europe/Belgrade` - Europe/Belgrade
        * `Europe/Berlin` - Europe/Berlin
        * `Europe/Bratislava` - Europe/Bratislava
        * `Europe/Brussels` - Europe/Brussels
        * `Europe/Bucharest` - Europe/Bucharest
        * `Europe/Budapest` - Europe/Budapest
        * `Europe/Busingen` - Europe/Busingen
        * `Europe/Chisinau` - Europe/Chisinau
        * `Europe/Copenhagen` - Europe/Copenhagen
        * `Europe/Dublin` - Europe/Dublin
        * `Europe/Gibraltar` - Europe/Gibraltar
        * `Europe/Guernsey` - Europe/Guernsey
        * `Europe/Helsinki` - Europe/Helsinki
        * `Europe/Isle_of_Man` - Europe/Isle_of_Man
        * `Europe/Istanbul` - Europe/Istanbul
        * `Europe/Jersey` - Europe/Jersey
        * `Europe/Kaliningrad` - Europe/Kaliningrad
        * `Europe/Kiev` - Europe/Kiev
        * `Europe/Kirov` - Europe/Kirov
        * `Europe/Kyiv` - Europe/Kyiv
        * `Europe/Lisbon` - Europe/Lisbon
        * `Europe/Ljubljana` - Europe/Ljubljana
        * `Europe/London` - Europe/London
        * `Europe/Luxembourg` - Europe/Luxembourg
        * `Europe/Madrid` - Europe/Madrid
        * `Europe/Malta` - Europe/Malta
        * `Europe/Mariehamn` - Europe/Mariehamn
        * `Europe/Minsk` - Europe/Minsk
        * `Europe/Monaco` - Europe/Monaco
        * `Europe/Moscow` - Europe/Moscow
        * `Europe/Nicosia` - Europe/Nicosia
        * `Europe/Oslo` - Europe/Oslo
        * `Europe/Paris` - Europe/Paris
        * `Europe/Podgorica` - Europe/Podgorica
        * `Europe/Prague` - Europe/Prague
        * `Europe/Riga` - Europe/Riga
        * `Europe/Rome` - Europe/Rome
        * `Europe/Samara` - Europe/Samara
        * `Europe/San_Marino` - Europe/San_Marino
        * `Europe/Sarajevo` - Europe/Sarajevo
        * `Europe/Saratov` - Europe/Saratov
        * `Europe/Simferopol` - Europe/Simferopol
        * `Europe/Skopje` - Europe/Skopje
        * `Europe/Sofia` - Europe/Sofia
        * `Europe/Stockholm` - Europe/Stockholm
        * `Europe/Tallinn` - Europe/Tallinn
        * `Europe/Tirane` - Europe/Tirane
        * `Europe/Tiraspol` - Europe/Tiraspol
        * `Europe/Ulyanovsk` - Europe/Ulyanovsk
        * `Europe/Uzhgorod` - Europe/Uzhgorod
        * `Europe/Vaduz` - Europe/Vaduz
        * `Europe/Vatican` - Europe/Vatican
        * `Europe/Vienna` - Europe/Vienna
        * `Europe/Vilnius` - Europe/Vilnius
        * `Europe/Volgograd` - Europe/Volgograd
        * `Europe/Warsaw` - Europe/Warsaw
        * `Europe/Zagreb` - Europe/Zagreb
        * `Europe/Zaporozhye` - Europe/Zaporozhye
        * `Europe/Zurich` - Europe/Zurich
        * `GB` - GB
        * `GB-Eire` - GB-Eire
        * `GMT` - GMT
        * `GMT+0` - GMT+0
        * `GMT-0` - GMT-0
        * `GMT0` - GMT0
        * `Greenwich` - Greenwich
        * `HST` - HST
        * `Hongkong` - Hongkong
        * `Iceland` - Iceland
        * `Indian/Antananarivo` - Indian/Antananarivo
        * `Indian/Chagos` - Indian/Chagos
        * `Indian/Christmas` - Indian/Christmas
        * `Indian/Cocos` - Indian/Cocos
        * `Indian/Comoro` - Indian/Comoro
        * `Indian/Kerguelen` - Indian/Kerguelen
        * `Indian/Mahe` - Indian/Mahe
        * `Indian/Maldives` - Indian/Maldives
        * `Indian/Mauritius` - Indian/Mauritius
        * `Indian/Mayotte` - Indian/Mayotte
        * `Indian/Reunion` - Indian/Reunion
        * `Iran` - Iran
        * `Israel` - Israel
        * `Jamaica` - Jamaica
        * `Japan` - Japan
        * `Kwajalein` - Kwajalein
        * `Libya` - Libya
        * `MET` - MET
        * `MST` - MST
        * `MST7MDT` - MST7MDT
        * `Mexico/BajaNorte` - Mexico/BajaNorte
        * `Mexico/BajaSur` - Mexico/BajaSur
        * `Mexico/General` - Mexico/General
        * `NZ` - NZ
        * `NZ-CHAT` - NZ-CHAT
        * `Navajo` - Navajo
        * `PRC` - PRC
        * `PST8PDT` - PST8PDT
        * `Pacific/Apia` - Pacific/Apia
        * `Pacific/Auckland` - Pacific/Auckland
        * `Pacific/Bougainville` - Pacific/Bougainville
        * `Pacific/Chatham` - Pacific/Chatham
        * `Pacific/Chuuk` - Pacific/Chuuk
        * `Pacific/Easter` - Pacific/Easter
        * `Pacific/Efate` - Pacific/Efate
        * `Pacific/Enderbury` - Pacific/Enderbury
        * `Pacific/Fakaofo` - Pacific/Fakaofo
        * `Pacific/Fiji` - Pacific/Fiji
        * `Pacific/Funafuti` - Pacific/Funafuti
        * `Pacific/Galapagos` - Pacific/Galapagos
        * `Pacific/Gambier` - Pacific/Gambier
        * `Pacific/Guadalcanal` - Pacific/Guadalcanal
        * `Pacific/Guam` - Pacific/Guam
        * `Pacific/Honolulu` - Pacific/Honolulu
        * `Pacific/Johnston` - Pacific/Johnston
        * `Pacific/Kanton` - Pacific/Kanton
        * `Pacific/Kiritimati` - Pacific/Kiritimati
        * `Pacific/Kosrae` - Pacific/Kosrae
        * `Pacific/Kwajalein` - Pacific/Kwajalein
        * `Pacific/Majuro` - Pacific/Majuro
        * `Pacific/Marquesas` - Pacific/Marquesas
        * `Pacific/Midway` - Pacific/Midway
        * `Pacific/Nauru` - Pacific/Nauru
        * `Pacific/Niue` - Pacific/Niue
        * `Pacific/Norfolk` - Pacific/Norfolk
        * `Pacific/Noumea` - Pacific/Noumea
        * `Pacific/Pago_Pago` - Pacific/Pago_Pago
        * `Pacific/Palau` - Pacific/Palau
        * `Pacific/Pitcairn` - Pacific/Pitcairn
        * `Pacific/Pohnpei` - Pacific/Pohnpei
        * `Pacific/Ponape` - Pacific/Ponape
        * `Pacific/Port_Moresby` - Pacific/Port_Moresby
        * `Pacific/Rarotonga` - Pacific/Rarotonga
        * `Pacific/Saipan` - Pacific/Saipan
        * `Pacific/Samoa` - Pacific/Samoa
        * `Pacific/Tahiti` - Pacific/Tahiti
        * `Pacific/Tarawa` - Pacific/Tarawa
        * `Pacific/Tongatapu` - Pacific/Tongatapu
        * `Pacific/Truk` - Pacific/Truk
        * `Pacific/Wake` - Pacific/Wake
        * `Pacific/Wallis` - Pacific/Wallis
        * `Pacific/Yap` - Pacific/Yap
        * `Poland` - Poland
        * `Portugal` - Portugal
        * `ROC` - ROC
        * `ROK` - ROK
        * `Singapore` - Singapore
        * `Turkey` - Turkey
        * `UCT` - UCT
        * `US/Alaska` - US/Alaska
        * `US/Aleutian` - US/Aleutian
        * `US/Arizona` - US/Arizona
        * `US/Central` - US/Central
        * `US/East-Indiana` - US/East-Indiana
        * `US/Eastern` - US/Eastern
        * `US/Hawaii` - US/Hawaii
        * `US/Indiana-Starke` - US/Indiana-Starke
        * `US/Michigan` - US/Michigan
        * `US/Mountain` - US/Mountain
        * `US/Pacific` - US/Pacific
        * `US/Samoa` - US/Samoa
        * `UTC` - UTC
        * `Universal` - Universal
        * `W-SU` - W-SU
        * `WET` - WET
        * `Zulu` - Zulu
            data_attributes (string): data_attributes
            person_display_name_properties (array): person_display_name_properties
            correlation_config (string): correlation_config
            autocapture_opt_out (boolean): autocapture_opt_out
            autocapture_exceptions_opt_in (boolean): autocapture_exceptions_opt_in
            autocapture_web_vitals_opt_in (boolean): autocapture_web_vitals_opt_in
            autocapture_web_vitals_allowed_metrics (string): autocapture_web_vitals_allowed_metrics
            autocapture_exceptions_errors_to_ignore (string): autocapture_exceptions_errors_to_ignore
            capture_console_log_opt_in (boolean): capture_console_log_opt_in
            capture_performance_opt_in (boolean): capture_performance_opt_in
            session_recording_opt_in (boolean): session_recording_opt_in
            session_recording_sample_rate (string): session_recording_sample_rate
            session_recording_minimum_duration_milliseconds (integer): session_recording_minimum_duration_milliseconds
            session_recording_linked_flag (string): session_recording_linked_flag
            session_recording_network_payload_capture_config (string): session_recording_network_payload_capture_config
            session_recording_masking_config (string): session_recording_masking_config
            session_replay_config (string): session_replay_config
            survey_config (string): survey_config
            access_control (boolean): access_control
            week_start_day (string): week_start_day
            primary_dashboard (integer): primary_dashboard
            live_events_columns (array): live_events_columns
            recording_domains (array): recording_domains
            person_on_events_querying_enabled (string): person_on_events_querying_enabled
            inject_web_apps (boolean): inject_web_apps
            extra_settings (string): extra_settings
            modifiers (string): modifiers
            default_modifiers (string): default_modifiers
            has_completed_onboarding_for (string): has_completed_onboarding_for
            surveys_opt_in (boolean): surveys_opt_in
            heatmaps_opt_in (boolean): heatmaps_opt_in
            product_intents (string): product_intents
            flags_persistence_default (boolean): flags_persistence_default

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, projects
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "organization": organization,
            "name": name,
            "product_description": product_description,
            "created_at": created_at,
            "effective_membership_level": effective_membership_level,
            "has_group_types": has_group_types,
            "group_types": group_types,
            "live_events_token": live_events_token,
            "updated_at": updated_at,
            "uuid": uuid,
            "api_token": api_token,
            "app_urls": app_urls,
            "slack_incoming_webhook": slack_incoming_webhook,
            "anonymize_ips": anonymize_ips,
            "completed_snippet_onboarding": completed_snippet_onboarding,
            "ingested_event": ingested_event,
            "test_account_filters": test_account_filters,
            "test_account_filters_default_checked": test_account_filters_default_checked,
            "path_cleaning_filters": path_cleaning_filters,
            "is_demo": is_demo,
            "timezone": timezone,
            "data_attributes": data_attributes,
            "person_display_name_properties": person_display_name_properties,
            "correlation_config": correlation_config,
            "autocapture_opt_out": autocapture_opt_out,
            "autocapture_exceptions_opt_in": autocapture_exceptions_opt_in,
            "autocapture_web_vitals_opt_in": autocapture_web_vitals_opt_in,
            "autocapture_web_vitals_allowed_metrics": autocapture_web_vitals_allowed_metrics,
            "autocapture_exceptions_errors_to_ignore": autocapture_exceptions_errors_to_ignore,
            "capture_console_log_opt_in": capture_console_log_opt_in,
            "capture_performance_opt_in": capture_performance_opt_in,
            "session_recording_opt_in": session_recording_opt_in,
            "session_recording_sample_rate": session_recording_sample_rate,
            "session_recording_minimum_duration_milliseconds": session_recording_minimum_duration_milliseconds,
            "session_recording_linked_flag": session_recording_linked_flag,
            "session_recording_network_payload_capture_config": session_recording_network_payload_capture_config,
            "session_recording_masking_config": session_recording_masking_config,
            "session_replay_config": session_replay_config,
            "survey_config": survey_config,
            "access_control": access_control,
            "week_start_day": week_start_day,
            "primary_dashboard": primary_dashboard,
            "live_events_columns": live_events_columns,
            "recording_domains": recording_domains,
            "person_on_events_querying_enabled": person_on_events_querying_enabled,
            "inject_web_apps": inject_web_apps,
            "extra_settings": extra_settings,
            "modifiers": modifiers,
            "default_modifiers": default_modifiers,
            "has_completed_onboarding_for": has_completed_onboarding_for,
            "surveys_opt_in": surveys_opt_in,
            "heatmaps_opt_in": heatmaps_opt_in,
            "product_intents": product_intents,
            "flags_persistence_default": flags_persistence_default,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/projects/{id}/reset_token/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def proxy_records_list(
        self, organization_id, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of proxy records for a specified organization using query parameters for limit and offset.

        Args:
            organization_id (string): organization_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, proxy_records
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/proxy_records/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def proxy_records_create(
        self,
        organization_id,
        id,
        domain,
        target_cname,
        status,
        message,
        created_at,
        updated_at,
        created_by,
    ) -> dict[str, Any]:
        """
        Creates a proxy record for the specified organization using the provided organization ID.

        Args:
            organization_id (string): organization_id
            id (string): id
            domain (string): domain
            target_cname (string): target_cname
            status (string): status
            message (string): message
            created_at (string): created_at
            updated_at (string): updated_at
            created_by (integer): created_by

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, proxy_records
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        request_body = {
            "id": id,
            "domain": domain,
            "target_cname": target_cname,
            "status": status,
            "message": message,
            "created_at": created_at,
            "updated_at": updated_at,
            "created_by": created_by,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/proxy_records/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def proxy_records_retrieve(self, organization_id, id) -> dict[str, Any]:
        """
        Retrieves a specific proxy record by its ID for a given organization using the PostHog API.

        Args:
            organization_id (string): organization_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, proxy_records
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/proxy_records/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def proxy_records_update(
        self,
        organization_id,
        id,
        id_body,
        domain,
        target_cname,
        status,
        message,
        created_at,
        updated_at,
        created_by,
    ) -> dict[str, Any]:
        """
        Updates a specific proxy record within an organization using the provided identifier and returns a status upon success.

        Args:
            organization_id (string): organization_id
            id (string): id
            id_body (string): id
            domain (string): domain
            target_cname (string): target_cname
            status (string): status
            message (string): message
            created_at (string): created_at
            updated_at (string): updated_at
            created_by (integer): created_by

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, proxy_records
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "domain": domain,
            "target_cname": target_cname,
            "status": status,
            "message": message,
            "created_at": created_at,
            "updated_at": updated_at,
            "created_by": created_by,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/proxy_records/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def proxy_records_partial_update(
        self,
        organization_id,
        id,
        id_body=None,
        domain=None,
        target_cname=None,
        status=None,
        message=None,
        created_at=None,
        updated_at=None,
        created_by=None,
    ) -> dict[str, Any]:
        """
        Updates a proxy record for an organization using the provided ID and organization ID, and returns a status message.

        Args:
            organization_id (string): organization_id
            id (string): id
            id_body (string): id
            domain (string): domain
            target_cname (string): target_cname
            status (string): status
            message (string): message
            created_at (string): created_at
            updated_at (string): updated_at
            created_by (integer): created_by

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, proxy_records
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "domain": domain,
            "target_cname": target_cname,
            "status": status,
            "message": message,
            "created_at": created_at,
            "updated_at": updated_at,
            "created_by": created_by,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/proxy_records/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def proxy_records_destroy(self, organization_id, id) -> Any:
        """
        Deletes a specific proxy record identified by `{id}` within an organization specified by `{organization_id}` using the `DELETE` method.

        Args:
            organization_id (string): organization_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            organizations, proxy_records
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/proxy_records/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_list(self, organization_id, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a list of roles for a specified organization using the provided organization ID, with optional parameters to limit and offset the results.

        Args:
            organization_id (string): organization_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_create(
        self,
        organization_id,
        id,
        name,
        created_at,
        created_by,
        members,
        feature_flags_access_level=None,
    ) -> dict[str, Any]:
        """
        Creates a new role within the specified organization and returns the created resource upon success.

        Args:
            organization_id (string): organization_id
            id (string): id
            name (string): name
            created_at (string): created_at
            created_by (string): created_by
            members (string): members
            feature_flags_access_level (string): feature_flags_access_level

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        request_body = {
            "id": id,
            "name": name,
            "feature_flags_access_level": feature_flags_access_level,
            "created_at": created_at,
            "created_by": created_by,
            "members": members,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_retrieve(self, organization_id, id) -> dict[str, Any]:
        """
        Retrieves a specific role within an organization based on the role and organization identifiers.

        Args:
            organization_id (string): organization_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_update(
        self,
        organization_id,
        id,
        id_body,
        name,
        created_at,
        created_by,
        members,
        feature_flags_access_level=None,
    ) -> dict[str, Any]:
        """
        Updates a specific role in an organization using the provided role ID and organization ID.

        Args:
            organization_id (string): organization_id
            id (string): id
            id_body (string): id
            name (string): name
            created_at (string): created_at
            created_by (string): created_by
            members (string): members
            feature_flags_access_level (string): feature_flags_access_level

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "feature_flags_access_level": feature_flags_access_level,
            "created_at": created_at,
            "created_by": created_by,
            "members": members,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_partial_update(
        self,
        organization_id,
        id,
        id_body=None,
        name=None,
        feature_flags_access_level=None,
        created_at=None,
        created_by=None,
        members=None,
    ) -> dict[str, Any]:
        """
        Updates the specified role within an organization using partial modifications via the PATCH method and returns a success response.

        Args:
            organization_id (string): organization_id
            id (string): id
            id_body (string): id
            name (string): name
            feature_flags_access_level (string): feature_flags_access_level
            created_at (string): created_at
            created_by (string): created_by
            members (string): members

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "feature_flags_access_level": feature_flags_access_level,
            "created_at": created_at,
            "created_by": created_by,
            "members": members,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_destroy(self, organization_id, id) -> Any:
        """
        Removes a specific role from an organization by its ID using a DELETE request and returns a 204 No Content response upon success.

        Args:
            organization_id (string): organization_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_role_memberships_list(
        self, organization_id, role_id, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of role memberships for a specific role within an organization using query parameters for limit and offset.

        Args:
            organization_id (string): organization_id
            role_id (string): role_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if role_id is None:
            raise ValueError("Missing required parameter 'role_id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{role_id}/role_memberships/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_role_memberships_create(
        self,
        organization_id,
        role_id,
        id,
        role_id_body,
        organization_member,
        user,
        joined_at,
        updated_at,
        user_uuid,
    ) -> dict[str, Any]:
        """
        Assigns a role to an organization member by associating the role ID with the membership via a POST request.

        Args:
            organization_id (string): organization_id
            role_id (string): role_id
            id (string): id
            role_id_body (string): role_id
            organization_member (string): organization_member
            user (string): user
            joined_at (string): joined_at
            updated_at (string): updated_at
            user_uuid (string): user_uuid

        Returns:
            dict[str, Any]: API response data.

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if role_id is None:
            raise ValueError("Missing required parameter 'role_id'")
        request_body = {
            "id": id,
            "role_id": role_id_body,
            "organization_member": organization_member,
            "user": user,
            "joined_at": joined_at,
            "updated_at": updated_at,
            "user_uuid": user_uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{role_id}/role_memberships/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def roles_role_memberships_destroy(self, organization_id, role_id, id) -> Any:
        """
        Removes a specific role membership from an organization role using the provided organization ID, role ID, and membership ID.

        Args:
            organization_id (string): organization_id
            role_id (string): role_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            organizations, roles
        """
        if organization_id is None:
            raise ValueError("Missing required parameter 'organization_id'")
        if role_id is None:
            raise ValueError("Missing required parameter 'role_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/organizations/{organization_id}/roles/{role_id}/role_memberships/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def actions_list(
        self, project_id, format=None, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of actions for a specified project using the "GET" method, allowing optional filtering by format, limit, and offset.

        Args:
            project_id (string): project_id
            format (string): Specifies the response format for the action results.
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            actions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/actions/"
        query_params = {
            k: v
            for k, v in [("format", format), ("limit", limit), ("offset", offset)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def actions_create(
        self,
        project_id,
        format=None,
        id=None,
        name=None,
        description=None,
        tags=None,
        post_to_slack=None,
        slack_message_format=None,
        steps=None,
        created_at=None,
        created_by=None,
        deleted=None,
        is_calculating=None,
        last_calculated_at=None,
        team_id=None,
        is_action=None,
        bytecode_error=None,
        pinned_at=None,
        creation_context=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Creates an action for a specified project using the POST method and returns a status message upon success.

        Args:
            project_id (string): project_id
            format (string): The format of the response data (e.g., JSON, XML).
            id (integer): id
            name (string): name
            description (string): description
            tags (array): tags
            post_to_slack (boolean): post_to_slack
            slack_message_format (string): slack_message_format
            steps (array): steps
            created_at (string): created_at
            created_by (string): created_by
            deleted (boolean): deleted
            is_calculating (boolean): is_calculating
            last_calculated_at (string): last_calculated_at
            team_id (integer): team_id
            is_action (boolean): is_action
            bytecode_error (string): bytecode_error
            pinned_at (string): pinned_at
            creation_context (string): creation_context
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            actions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "description": description,
            "tags": tags,
            "post_to_slack": post_to_slack,
            "slack_message_format": slack_message_format,
            "steps": steps,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "is_calculating": is_calculating,
            "last_calculated_at": last_calculated_at,
            "team_id": team_id,
            "is_action": is_action,
            "bytecode_error": bytecode_error,
            "pinned_at": pinned_at,
            "creation_context": creation_context,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/actions/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_list(
        self,
        project_id,
        contains=None,
        created_by=None,
        date_from=None,
        date_to=None,
        limit=None,
        offset=None,
        user=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of notebooks for a specific project with optional filtering by content, creator, date range, and pagination parameters.

        Args:
            project_id (string): project_id
            contains (string): Filter for notebooks that match a provided filter. Each match pair is separated by a colon, multiple match pairs can be sent separated by a space or a comma
            created_by (integer): The UUID of the Notebook's creator
            date_from (string): Filter for notebooks created after this date & time
            date_to (string): Filter for notebooks created before this date & time
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.
            user (string): If any value is provided for this parameter, return notebooks created by the logged in user.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/"
        query_params = {
            k: v
            for k, v in [
                ("contains", contains),
                ("created_by", created_by),
                ("date_from", date_from),
                ("date_to", date_to),
                ("limit", limit),
                ("offset", offset),
                ("user", user),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_create(
        self,
        project_id,
        id=None,
        short_id=None,
        title=None,
        content=None,
        text_content=None,
        version=None,
        deleted=None,
        created_at=None,
        created_by=None,
        last_modified_at=None,
        last_modified_by=None,
        user_access_level=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Creates a new notebook for a specified project using the project ID.

        Args:
            project_id (string): project_id
            id (string): id
            short_id (string): short_id
            title (string): title
            content (string): content
            text_content (string): text_content
            version (integer): version
            deleted (boolean): deleted
            created_at (string): created_at
            created_by (string): created_by
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            user_access_level (string): The effective access level the user has for this object
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "short_id": short_id,
            "title": title,
            "content": content,
            "text_content": text_content,
            "version": version,
            "deleted": deleted,
            "created_at": created_at,
            "created_by": created_by,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "user_access_level": user_access_level,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_retrieve(self, project_id, short_id) -> dict[str, Any]:
        """
        Retrieves the details of a specific notebook identified by its short ID within a given project.

        Args:
            project_id (string): project_id
            short_id (string): short_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/{short_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_update(
        self,
        project_id,
        short_id,
        id=None,
        short_id_body=None,
        title=None,
        content=None,
        text_content=None,
        version=None,
        deleted=None,
        created_at=None,
        created_by=None,
        last_modified_at=None,
        last_modified_by=None,
        user_access_level=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Updates a notebook in the specified project and returns a success status.

        Args:
            project_id (string): project_id
            short_id (string): short_id
            id (string): id
            short_id_body (string): short_id
            title (string): title
            content (string): content
            text_content (string): text_content
            version (integer): version
            deleted (boolean): deleted
            created_at (string): created_at
            created_by (string): created_by
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            user_access_level (string): The effective access level the user has for this object
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        request_body = {
            "id": id,
            "short_id": short_id_body,
            "title": title,
            "content": content,
            "text_content": text_content,
            "version": version,
            "deleted": deleted,
            "created_at": created_at,
            "created_by": created_by,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "user_access_level": user_access_level,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/{short_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_partial_update(
        self,
        project_id,
        short_id,
        id=None,
        short_id_body=None,
        title=None,
        content=None,
        text_content=None,
        version=None,
        deleted=None,
        created_at=None,
        created_by=None,
        last_modified_at=None,
        last_modified_by=None,
        user_access_level=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Updates a notebook identified by its project ID and short ID using the provided data.

        Args:
            project_id (string): project_id
            short_id (string): short_id
            id (string): id
            short_id_body (string): short_id
            title (string): title
            content (string): content
            text_content (string): text_content
            version (integer): version
            deleted (boolean): deleted
            created_at (string): created_at
            created_by (string): created_by
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            user_access_level (string): The effective access level the user has for this object
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        request_body = {
            "id": id,
            "short_id": short_id_body,
            "title": title,
            "content": content,
            "text_content": text_content,
            "version": version,
            "deleted": deleted,
            "created_at": created_at,
            "created_by": created_by,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "user_access_level": user_access_level,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/{short_id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_destroy(self, project_id, short_id) -> Any:
        """
        Deletes a notebook specified by its short ID from a project identified by its project ID using the API.

        Args:
            project_id (string): project_id
            short_id (string): short_id

        Returns:
            Any: API response data.

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/{short_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_activity_retrieve_2(self, project_id, short_id) -> Any:
        """
        Retrieves the activity history for a specific notebook within a project.

        Args:
            project_id (string): project_id
            short_id (string): short_id

        Returns:
            Any: No response body

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = (
            f"{self.base_url}/api/projects/{project_id}/notebooks/{short_id}/activity/"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_activity_retrieve(self, project_id) -> Any:
        """
        Retrieves activity information for a notebook within a specified project.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/activity/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def notebooks_recording_comments_retrieve(self, project_id) -> Any:
        """
        Retrieves a list of recording comments associated with a specific project by its ID.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            notebooks
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/notebooks/recording_comments/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_list(
        self,
        project_id,
        distinct_id=None,
        email=None,
        format=None,
        limit=None,
        offset=None,
        properties=None,
        search=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of persons associated with a specific project, optionally filtered by distinct ID, email, properties, or search criteria.

        Args:
            project_id (string): project_id
            distinct_id (string): Filter list by distinct id.
            email (string): Filter persons by email (exact match)
            format (string): Specifies the response format for the returned data (e.g., JSON, XML, CSV).
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.
            properties (array): Filter Persons by person properties.
            search (string): Search persons, either by email (full text search) or distinct_id (exact match).

        Returns:
            dict[str, Any]: API response data.

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/"
        query_params = {
            k: v
            for k, v in [
                ("distinct_id", distinct_id),
                ("email", email),
                ("format", format),
                ("limit", limit),
                ("offset", offset),
                ("properties", properties),
                ("search", search),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_retrieve(self, project_id, id, format=None) -> dict[str, Any]:
        """
        Retrieves a specific person's details from a project using their ID and allows optional response formatting.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): Specifies the output format of the response for the specified person within a project.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_update(
        self,
        project_id,
        id,
        format=None,
        id_body=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> dict[str, Any]:
        """
        Updates a specific person's details within a designated project and returns a success response upon completion.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): Defines the output format for the response data in the PUT operation.
            id_body (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            dict[str, Any]: API response data.

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_partial_update(
        self,
        project_id,
        id,
        format=None,
        id_body=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> dict[str, Any]:
        """
        Updates the details of a specific person associated with a project using the PATCH method, allowing for partial modification of the person's information.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): Specifies the format of the response data for the PATCH operation (e.g., JSON, XML).
            id_body (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            dict[str, Any]: API response data.

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_destroy(self, project_id, id, delete_events=None, format=None) -> Any:
        """
        Deletes a specific person within a project, optionally removing associated events, without returning content.

        Args:
            project_id (string): project_id
            id (string): id
            delete_events (boolean): If true, a task to delete all events associated with this person will be created and queued. The task does not run immediately and instead is batched together and at 5AM UTC every Sunday
            format (string): Specifies the response format (e.g., JSON, XML) for the deleted person resource.

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/"
        query_params = {
            k: v
            for k, v in [("delete_events", delete_events), ("format", format)]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_activity_retrieve_2(self, project_id, id, format=None) -> Any:
        """
        Retrieves activity information for a specific person within a project using the "GET" method.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): Specifies the desired response format (e.g., JSON, XML).

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/activity/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_delete_events_create(
        self,
        project_id,
        id,
        format=None,
        id_body=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Deletes events associated with a person in a project using the POST method and returns a status message.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): Specifies the format of the response data (e.g., JSON, XML).
            id_body (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/delete_events/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_delete_property_create(
        self,
        project_id,
        id,
        unset,
        format=None,
        id_body=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Removes a specified property from a person within a project using a POST request, returning a success status on completion.

        Args:
            project_id (string): project_id
            id (string): id
            unset (string): Specify the property key to delete
            format (string): Specifies the response media format (e.g., JSON, XML) for the operation.
            id_body (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/delete_property/"
        query_params = {
            k: v for k, v in [("$unset", unset), ("format", format)] if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_properties_timeline_retrieve(self, project_id, id, format=None) -> Any:
        """
        Retrieves a timeline of property changes for a specific person in a project, optionally formatted.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): The format of the response data (e.g., `json` or `xml`).

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/properties_timeline/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_split_create(
        self,
        project_id,
        id,
        format=None,
        id_body=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Splits a specified person into separate entities within a project and returns the operation result.

        Args:
            project_id (string): project_id
            id (string): id
            format (string): The format of the response, specified as a query parameter.
            id_body (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/split/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_update_property_create(
        self,
        project_id,
        id,
        key,
        value,
        format=None,
        id_body=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Updates a property for a specified person within a project using the provided key and value.

        Args:
            project_id (string): project_id
            id (string): id
            key (string): Specify the property key
            value (string): Specify the property value
            format (string): The format parameter specifies the output format for the response.
            id_body (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/{id}/update_property/"
        query_params = {
            k: v
            for k, v in [("format", format), ("key", key), ("value", value)]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_activity_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves activity data for persons associated with a specific project in the requested format.

        Args:
            project_id (string): project_id
            format (string): Specifies the format of the response data for the activity of persons in a project.

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/activity/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_bulk_delete_create(
        self,
        project_id,
        delete_events=None,
        distinct_ids=None,
        format=None,
        ids=None,
        id=None,
        name=None,
        distinct_ids_body=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Deletes multiple persons from a project in bulk using their IDs or distinct IDs, optionally including the deletion of associated events, via a POST request to `/api/projects/{project_id}/persons/bulk_delete/`.

        Args:
            project_id (string): project_id
            delete_events (boolean): If true, a task to delete all events associated with this person will be created and queued. The task does not run immediately and instead is batched together and at 5AM UTC every Sunday
            distinct_ids (object): A list of distinct IDs, up to 1000 of them. We'll delete all persons associated with those distinct IDs.
            format (string): Specifies the format (e.g., JSON, XML) for the response data from the bulk delete operation.
            ids (object): A list of PostHog person IDs, up to 1000 of them. We'll delete all the persons listed.
            id (integer): id
            name (string): name
            distinct_ids_body (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "distinct_ids": distinct_ids_body,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/bulk_delete/"
        query_params = {
            k: v
            for k, v in [
                ("delete_events", delete_events),
                ("distinct_ids", distinct_ids),
                ("format", format),
                ("ids", ids),
            ]
            if v is not None
        }
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_cohorts_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves a list of person cohorts for a specified project using the provided project ID.

        Args:
            project_id (string): project_id
            format (string): Specifies the output format for the response.

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/cohorts/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_funnel_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves a list of persons in a funnel for a specific project using the project ID and optionally formats the output.

        Args:
            project_id (string): project_id
            format (string): Specifies the output format for the response, allowing clients to request data in a specific format.

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/funnel/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_funnel_create(
        self,
        project_id,
        format=None,
        id=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Tracks user funnel data for a specific project and returns formatted results.

        Args:
            project_id (string): project_id
            format (string): The output format for the funnel data (e.g., json, csv).
            id (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/funnel/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_funnel_correlation_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves correlation data for persons in a project, identified by the project ID, and optionally formats the output based on the specified format parameter.

        Args:
            project_id (string): project_id
            format (string): The format for the response data (e.g., JSON, XML).

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/funnel/correlation/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_funnel_correlation_create(
        self,
        project_id,
        format=None,
        id=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Calculates and returns the correlation between funnel data for individuals within a specified project using the POST method.

        Args:
            project_id (string): project_id
            format (string): The format parameter specifies the output format for the correlation data.
            id (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/funnel/correlation/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_lifecycle_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves lifecycle information for persons associated with a project, identified by the specified project ID, allowing optional format specification.

        Args:
            project_id (string): project_id
            format (string): Specifies the output format for the lifecycle data of persons in a project.

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/lifecycle/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_reset_person_distinct_id_create(
        self,
        project_id,
        format=None,
        id=None,
        name=None,
        distinct_ids=None,
        properties=None,
        created_at=None,
        uuid=None,
    ) -> Any:
        """
        Resets and unlinks a person's distinct identifier in the specified project, clearing associated user data across devices or sessions.

        Args:
            project_id (string): project_id
            format (string): The format of the response, specified in the query string.
            id (integer): id
            name (string): name
            distinct_ids (array): distinct_ids
            properties (string): properties
            created_at (string): created_at
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "distinct_ids": distinct_ids,
            "properties": properties,
            "created_at": created_at,
            "uuid": uuid,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/persons/reset_person_distinct_id/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_stickiness_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves stickiness data for persons associated with a specific project, optionally formatted.

        Args:
            project_id (string): project_id
            format (string): The output format for the response data (e.g., JSON, XML).

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/stickiness/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_trends_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves trends related to persons in a specified project using the GET method and returns the data in a requested format.

        Args:
            project_id (string): project_id
            format (string): Specifies the format (e.g., JSON, CSV) for the response data of project person trends.

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/trends/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def persons_values_retrieve(self, project_id, format=None) -> Any:
        """
        Retrieves a list of person values for a specified project using the provided project ID.

        Args:
            project_id (string): project_id
            format (string): Specifies the format in which the data should be returned (e.g., JSON, XML, CSV).

        Returns:
            Any: No response body

        Tags:
            persons
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/persons/values/"
        query_params = {k: v for k, v in [("format", format)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def plugin_configs_logs_list(
        self, project_id, plugin_config_id, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves and returns log entries for a specific plugin configuration within a project, allowing pagination through query parameters for limit and offset.

        Args:
            project_id (string): project_id
            plugin_config_id (string): plugin_config_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            plugin_configs
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if plugin_config_id is None:
            raise ValueError("Missing required parameter 'plugin_config_id'")
        url = f"{self.base_url}/api/projects/{project_id}/plugin_configs/{plugin_config_id}/logs/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def property_definitions_list(
        self,
        project_id,
        event_names=None,
        exclude_core_properties=None,
        exclude_hidden=None,
        excluded_properties=None,
        filter_by_event_names=None,
        group_type_index=None,
        is_feature_flag=None,
        is_numerical=None,
        limit=None,
        offset=None,
        properties=None,
        search=None,
        type=None,
    ) -> dict[str, Any]:
        """
        Retrieves property definitions for a specific project with optional filtering for event names, excluded properties, hidden status, numerical type, and feature flags.

        Args:
            project_id (string): project_id
            event_names (string): If sent, response value will have `is_seen_on_filtered_events` populated. JSON-encoded
            exclude_core_properties (boolean): Whether to exclude core properties
            exclude_hidden (boolean): Whether to exclude properties marked as hidden
            excluded_properties (string): JSON-encoded list of excluded properties
            filter_by_event_names (boolean): Whether to return only properties for events in `event_names`
            group_type_index (integer): What group type is the property for. Only should be set if `type=group`
            is_feature_flag (boolean): Whether to return only (or excluding) feature flag properties
            is_numerical (boolean): Whether to return only (or excluding) numerical property definitions
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.
            properties (string): Comma-separated list of properties to filter
            search (string): Searches properties by name
            type (string): What property definitions to return * `event` - event
        * `person` - person
        * `group` - group
        * `session` - session

        Returns:
            dict[str, Any]: API response data.

        Tags:
            property_definitions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/property_definitions/"
        query_params = {
            k: v
            for k, v in [
                ("event_names", event_names),
                ("exclude_core_properties", exclude_core_properties),
                ("exclude_hidden", exclude_hidden),
                ("excluded_properties", excluded_properties),
                ("filter_by_event_names", filter_by_event_names),
                ("group_type_index", group_type_index),
                ("is_feature_flag", is_feature_flag),
                ("is_numerical", is_numerical),
                ("limit", limit),
                ("offset", offset),
                ("properties", properties),
                ("search", search),
                ("type", type),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def property_definitions_retrieve(self, project_id, id) -> dict[str, Any]:
        """
        Retrieves a specific property definition by ID for a given project.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            property_definitions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/property_definitions/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def property_definitions_update(
        self,
        project_id,
        id,
        id_body,
        name,
        is_seen_on_filtered_events,
        is_numerical=None,
        property_type=None,
        tags=None,
    ) -> dict[str, Any]:
        """
        Updates or replaces a specific property definition within a project using the PUT method, where the project and property definition are identified by their respective IDs.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            name (string): name
            is_seen_on_filtered_events (string): is_seen_on_filtered_events
            is_numerical (boolean): is_numerical
            property_type (string): property_type
            tags (array): tags

        Returns:
            dict[str, Any]: API response data.

        Tags:
            property_definitions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "is_numerical": is_numerical,
            "property_type": property_type,
            "tags": tags,
            "is_seen_on_filtered_events": is_seen_on_filtered_events,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/property_definitions/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def property_definitions_partial_update(
        self,
        project_id,
        id,
        id_body=None,
        name=None,
        is_numerical=None,
        property_type=None,
        tags=None,
        is_seen_on_filtered_events=None,
    ) -> dict[str, Any]:
        """
        Updates a specific property definition for a project using the "PATCH" method, allowing partial modifications to the resource at "/api/projects/{project_id}/property_definitions/{id}/".

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            name (string): name
            is_numerical (boolean): is_numerical
            property_type (string): property_type
            tags (array): tags
            is_seen_on_filtered_events (string): is_seen_on_filtered_events

        Returns:
            dict[str, Any]: API response data.

        Tags:
            property_definitions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "is_numerical": is_numerical,
            "property_type": property_type,
            "tags": tags,
            "is_seen_on_filtered_events": is_seen_on_filtered_events,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/property_definitions/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def property_definitions_destroy(self, project_id, id) -> Any:
        """
        Deletes a specified property definition from a project using the provided project ID and property definition ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            property_definitions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/property_definitions/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def property_definitions_seen_together_retrieve(self, project_id) -> Any:
        """
        Retrieves property definitions that are commonly seen together for a specified project.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            property_definitions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/property_definitions/seen_together/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_create(
        self,
        project_id,
        query,
        async_=None,
        client_query_id=None,
        filters_override=None,
        refresh=None,
        variables_override=None,
    ) -> Any:
        """
        Submits a query to process or retrieve project-specific data and returns the results.

        Args:
            project_id (string): project_id
            query (string): Submit a JSON string representing a query for PostHog data analysis, for example a HogQL query.

        Example payload:

        ```

        {"query": {"kind": "HogQLQuery", "query": "select * from events limit 100"}}

        ```

        For more details on HogQL queries, see the [PostHog HogQL documentation](/docs/hogql#api-access).
            async_ (string): async
            client_query_id (string): Client provided query ID. Can be used to retrieve the status or cancel the query.
            filters_override (string): filters_override
            refresh (string): Whether results should be calculated sync or async, and how much to rely on the cache:
        - `'blocking'` - calculate synchronously (returning only when the query is done), UNLESS there are very fresh results in the cache
        - `'async'` - kick off background calculation (returning immediately with a query status), UNLESS there are very fresh results in the cache
        - `'lazy_async'` - kick off background calculation, UNLESS there are somewhat fresh results in the cache
        - `'force_blocking'` - calculate synchronously, even if fresh results are already cached
        - `'force_async'` - kick off background calculation, even if fresh results are already cached
        - `'force_cache'` - return cached data or a cache miss; always completes immediately as it never calculates Background calculation can be tracked using the `query_status` response field.
            variables_override (string): variables_override

        Returns:
            Any: API response data.

        Tags:
            query
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "async": async_,
            "client_query_id": client_query_id,
            "filters_override": filters_override,
            "query": query,
            "refresh": refresh,
            "variables_override": variables_override,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/query/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_retrieve(self, project_id, id) -> dict[str, Any]:
        """
        Retrieves query details for a specific query within a project identified by the project ID and query ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            query
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/query/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_destroy(self, project_id, id) -> Any:
        """
        Deletes a query identified by the given ID within a specified project using the DELETE method and returns a successful response without content upon deletion.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: Query cancelled

        Tags:
            query
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/query/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_check_auth_for_async_create(self, project_id) -> Any:
        """
        Checks authorization for asynchronous operations on a specified project and returns the result.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            query
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/query/check_auth_for_async/"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_draft_sql_retrieve(self, project_id) -> Any:
        """
        Retrieves draft SQL queries for a specified project using the project's ID.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            query
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/query/draft_sql/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_list(
        self, project_id, created_by=None, limit=None, offset=None, short_id=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of session recording playlists for a specified project, filtered by creator, short ID, or other parameters.

        Args:
            project_id (string): project_id
            created_by (integer): Filters session recording playlists to those created by the specified user.
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.
            short_id (string): Filter sessions by a specific short identifier.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/"
        query_params = {
            k: v
            for k, v in [
                ("created_by", created_by),
                ("limit", limit),
                ("offset", offset),
                ("short_id", short_id),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_create(
        self,
        project_id,
        id=None,
        short_id=None,
        name=None,
        derived_name=None,
        description=None,
        pinned=None,
        created_at=None,
        created_by=None,
        deleted=None,
        filters=None,
        last_modified_at=None,
        last_modified_by=None,
        recordings_counts=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Creates a new session recording playlist for a specified project, allowing users to organize session recordings, using the PostHog API.

        Args:
            project_id (string): project_id
            id (integer): id
            short_id (string): short_id
            name (string): name
            derived_name (string): derived_name
            description (string): description
            pinned (boolean): pinned
            created_at (string): created_at
            created_by (string): created_by
            deleted (boolean): deleted
            filters (string): filters
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            recordings_counts (object): recordings_counts
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "short_id": short_id,
            "name": name,
            "derived_name": derived_name,
            "description": description,
            "pinned": pinned,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "filters": filters,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "recordings_counts": recordings_counts,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_retrieve(
        self, project_id, short_id
    ) -> dict[str, Any]:
        """
        Retrieves a session recording playlist by project ID and short ID using the GET method.

        Args:
            project_id (string): project_id
            short_id (string): short_id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_update(
        self,
        project_id,
        short_id,
        id=None,
        short_id_body=None,
        name=None,
        derived_name=None,
        description=None,
        pinned=None,
        created_at=None,
        created_by=None,
        deleted=None,
        filters=None,
        last_modified_at=None,
        last_modified_by=None,
        recordings_counts=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Updates a session recording playlist's configurations (name, description, filters, etc.) for a specified project and playlist identifier using the provided parameters.

        Args:
            project_id (string): project_id
            short_id (string): short_id
            id (integer): id
            short_id_body (string): short_id
            name (string): name
            derived_name (string): derived_name
            description (string): description
            pinned (boolean): pinned
            created_at (string): created_at
            created_by (string): created_by
            deleted (boolean): deleted
            filters (string): filters
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            recordings_counts (object): recordings_counts
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        request_body = {
            "id": id,
            "short_id": short_id_body,
            "name": name,
            "derived_name": derived_name,
            "description": description,
            "pinned": pinned,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "filters": filters,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "recordings_counts": recordings_counts,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_partial_update(
        self,
        project_id,
        short_id,
        id=None,
        short_id_body=None,
        name=None,
        derived_name=None,
        description=None,
        pinned=None,
        created_at=None,
        created_by=None,
        deleted=None,
        filters=None,
        last_modified_at=None,
        last_modified_by=None,
        recordings_counts=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Updates a session recording playlist for a specific project identified by project_id and playlist short_id.

        Args:
            project_id (string): project_id
            short_id (string): short_id
            id (integer): id
            short_id_body (string): short_id
            name (string): name
            derived_name (string): derived_name
            description (string): description
            pinned (boolean): pinned
            created_at (string): created_at
            created_by (string): created_by
            deleted (boolean): deleted
            filters (string): filters
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            recordings_counts (object): recordings_counts
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        request_body = {
            "id": id,
            "short_id": short_id_body,
            "name": name,
            "derived_name": derived_name,
            "description": description,
            "pinned": pinned,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "filters": filters,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "recordings_counts": recordings_counts,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_destroy(self, project_id, short_id) -> Any:
        """
        Deletes a session recording playlist in a specified project using its short identifier, returning a 405 status code (method not allowed for hard deletes).

        Args:
            project_id (string): project_id
            short_id (string): short_id

        Returns:
            Any: API response data.

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_recordings_retrieve(
        self, project_id, short_id
    ) -> Any:
        """
        Retrieves a list of recordings associated with a specific session recording playlist in a project.

        Args:
            project_id (string): project_id
            short_id (string): short_id

        Returns:
            Any: No response body

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_recordings_create(
        self,
        project_id,
        short_id,
        session_recording_id,
        id=None,
        short_id_body=None,
        name=None,
        derived_name=None,
        description=None,
        pinned=None,
        created_at=None,
        created_by=None,
        deleted=None,
        filters=None,
        last_modified_at=None,
        last_modified_by=None,
        recordings_counts=None,
        create_in_folder=None,
    ) -> Any:
        """
        Creates a new recording for a session recording playlist within a specified project using the provided session recording ID and short ID.

        Args:
            project_id (string): project_id
            short_id (string): short_id
            session_recording_id (string): session_recording_id
            id (integer): id
            short_id_body (string): short_id
            name (string): name
            derived_name (string): derived_name
            description (string): description
            pinned (boolean): pinned
            created_at (string): created_at
            created_by (string): created_by
            deleted (boolean): deleted
            filters (string): filters
            last_modified_at (string): last_modified_at
            last_modified_by (string): last_modified_by
            recordings_counts (object): recordings_counts
            create_in_folder (string): _create_in_folder

        Returns:
            Any: No response body

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        if session_recording_id is None:
            raise ValueError("Missing required parameter 'session_recording_id'")
        request_body = {
            "id": id,
            "short_id": short_id_body,
            "name": name,
            "derived_name": derived_name,
            "description": description,
            "pinned": pinned,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "filters": filters,
            "last_modified_at": last_modified_at,
            "last_modified_by": last_modified_by,
            "recordings_counts": recordings_counts,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recording_playlists_recordings_destroy(
        self, project_id, short_id, session_recording_id
    ) -> Any:
        """
        Deletes a specific session recording from a session recording playlist in a project using the provided project, playlist, and recording identifiers.

        Args:
            project_id (string): project_id
            short_id (string): short_id
            session_recording_id (string): session_recording_id

        Returns:
            Any: No response body

        Tags:
            session_recording_playlists
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if short_id is None:
            raise ValueError("Missing required parameter 'short_id'")
        if session_recording_id is None:
            raise ValueError("Missing required parameter 'session_recording_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_list(
        self, project_id, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of session recordings for a specified project, allowing pagination through limit and offset parameters.

        Args:
            project_id (string): project_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_retrieve(self, project_id, id) -> dict[str, Any]:
        """
        Retrieves a specific session recording for a project identified by project_id and session ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_update(
        self,
        project_id,
        id,
        id_body=None,
        distinct_id=None,
        viewed=None,
        viewers=None,
        recording_duration=None,
        active_seconds=None,
        inactive_seconds=None,
        start_time=None,
        end_time=None,
        click_count=None,
        keypress_count=None,
        mouse_activity_count=None,
        console_log_count=None,
        console_warn_count=None,
        console_error_count=None,
        start_url=None,
        person=None,
        storage=None,
        snapshot_source=None,
        ongoing=None,
        activity_score=None,
    ) -> dict[str, Any]:
        """
        Updates or replaces a specific session recording within a project using the provided ID and returns a success status upon completion.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            distinct_id (string): distinct_id
            viewed (boolean): viewed
            viewers (array): viewers
            recording_duration (integer): recording_duration
            active_seconds (integer): active_seconds
            inactive_seconds (integer): inactive_seconds
            start_time (string): start_time
            end_time (string): end_time
            click_count (integer): click_count
            keypress_count (integer): keypress_count
            mouse_activity_count (integer): mouse_activity_count
            console_log_count (integer): console_log_count
            console_warn_count (integer): console_warn_count
            console_error_count (integer): console_error_count
            start_url (string): start_url
            person (object): person
            storage (string): storage
            snapshot_source (string): snapshot_source
            ongoing (boolean): ongoing
            activity_score (number): activity_score

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "distinct_id": distinct_id,
            "viewed": viewed,
            "viewers": viewers,
            "recording_duration": recording_duration,
            "active_seconds": active_seconds,
            "inactive_seconds": inactive_seconds,
            "start_time": start_time,
            "end_time": end_time,
            "click_count": click_count,
            "keypress_count": keypress_count,
            "mouse_activity_count": mouse_activity_count,
            "console_log_count": console_log_count,
            "console_warn_count": console_warn_count,
            "console_error_count": console_error_count,
            "start_url": start_url,
            "person": person,
            "storage": storage,
            "snapshot_source": snapshot_source,
            "ongoing": ongoing,
            "activity_score": activity_score,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_partial_update(
        self,
        project_id,
        id,
        id_body=None,
        distinct_id=None,
        viewed=None,
        viewers=None,
        recording_duration=None,
        active_seconds=None,
        inactive_seconds=None,
        start_time=None,
        end_time=None,
        click_count=None,
        keypress_count=None,
        mouse_activity_count=None,
        console_log_count=None,
        console_warn_count=None,
        console_error_count=None,
        start_url=None,
        person=None,
        storage=None,
        snapshot_source=None,
        ongoing=None,
        activity_score=None,
    ) -> dict[str, Any]:
        """
        Updates the specified session recording within a project with partial modifications using the PATCH HTTP method.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            distinct_id (string): distinct_id
            viewed (boolean): viewed
            viewers (array): viewers
            recording_duration (integer): recording_duration
            active_seconds (integer): active_seconds
            inactive_seconds (integer): inactive_seconds
            start_time (string): start_time
            end_time (string): end_time
            click_count (integer): click_count
            keypress_count (integer): keypress_count
            mouse_activity_count (integer): mouse_activity_count
            console_log_count (integer): console_log_count
            console_warn_count (integer): console_warn_count
            console_error_count (integer): console_error_count
            start_url (string): start_url
            person (object): person
            storage (string): storage
            snapshot_source (string): snapshot_source
            ongoing (boolean): ongoing
            activity_score (number): activity_score

        Returns:
            dict[str, Any]: API response data.

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "distinct_id": distinct_id,
            "viewed": viewed,
            "viewers": viewers,
            "recording_duration": recording_duration,
            "active_seconds": active_seconds,
            "inactive_seconds": inactive_seconds,
            "start_time": start_time,
            "end_time": end_time,
            "click_count": click_count,
            "keypress_count": keypress_count,
            "mouse_activity_count": mouse_activity_count,
            "console_log_count": console_log_count,
            "console_warn_count": console_warn_count,
            "console_error_count": console_error_count,
            "start_url": start_url,
            "person": person,
            "storage": storage,
            "snapshot_source": snapshot_source,
            "ongoing": ongoing,
            "activity_score": activity_score,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_destroy(self, project_id, id) -> Any:
        """
        Deletes a specific session recording using the provided project ID and session recording ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_analyze_similar_retrieve(self, project_id, id) -> Any:
        """
        Analyzes a session recording for similar recordings within a specific project using the provided project ID and session recording ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/{id}/analyze/similar/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_sharing_list(self, project_id, recording_id) -> list[Any]:
        """
        Retrieves sharing details for a specific session recording within a project.

        Args:
            project_id (string): project_id
            recording_id (string): recording_id

        Returns:
            list[Any]: API response data.

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if recording_id is None:
            raise ValueError("Missing required parameter 'recording_id'")
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/{recording_id}/sharing/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def session_recordings_ai_regex_create(
        self,
        project_id,
        id=None,
        distinct_id=None,
        viewed=None,
        viewers=None,
        recording_duration=None,
        active_seconds=None,
        inactive_seconds=None,
        start_time=None,
        end_time=None,
        click_count=None,
        keypress_count=None,
        mouse_activity_count=None,
        console_log_count=None,
        console_warn_count=None,
        console_error_count=None,
        start_url=None,
        person=None,
        storage=None,
        snapshot_source=None,
        ongoing=None,
        activity_score=None,
    ) -> Any:
        """
        Creates AI-powered regex session recordings for a specified project using the POST method.

        Args:
            project_id (string): project_id
            id (string): id
            distinct_id (string): distinct_id
            viewed (boolean): viewed
            viewers (array): viewers
            recording_duration (integer): recording_duration
            active_seconds (integer): active_seconds
            inactive_seconds (integer): inactive_seconds
            start_time (string): start_time
            end_time (string): end_time
            click_count (integer): click_count
            keypress_count (integer): keypress_count
            mouse_activity_count (integer): mouse_activity_count
            console_log_count (integer): console_log_count
            console_warn_count (integer): console_warn_count
            console_error_count (integer): console_error_count
            start_url (string): start_url
            person (object): person
            storage (string): storage
            snapshot_source (string): snapshot_source
            ongoing (boolean): ongoing
            activity_score (number): activity_score

        Returns:
            Any: No response body

        Tags:
            session_recordings
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "distinct_id": distinct_id,
            "viewed": viewed,
            "viewers": viewers,
            "recording_duration": recording_duration,
            "active_seconds": active_seconds,
            "inactive_seconds": inactive_seconds,
            "start_time": start_time,
            "end_time": end_time,
            "click_count": click_count,
            "keypress_count": keypress_count,
            "mouse_activity_count": mouse_activity_count,
            "console_log_count": console_log_count,
            "console_warn_count": console_warn_count,
            "console_error_count": console_error_count,
            "start_url": start_url,
            "person": person,
            "storage": storage,
            "snapshot_source": snapshot_source,
            "ongoing": ongoing,
            "activity_score": activity_score,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/session_recordings/ai/regex/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sessions_property_definitions_retrieve(self, project_id) -> Any:
        """
        Retrieves property definitions associated with sessions for a specified project.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            sessions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = (
            f"{self.base_url}/api/projects/{project_id}/sessions/property_definitions/"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def sessions_values_retrieve(self, project_id) -> Any:
        """
        Retrieves session values for a specific project identified by its project_id.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            sessions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/sessions/values/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_list(self, project_id, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a list of subscriptions for a specified project by project ID, allowing pagination through query parameters for limit and offset.

        Args:
            project_id (string): project_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            subscriptions, important
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/subscriptions/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_create(
        self,
        project_id,
        id,
        target_type,
        target_value,
        frequency,
        start_date,
        created_at,
        created_by,
        summary,
        next_delivery_date,
        dashboard=None,
        insight=None,
        interval=None,
        byweekday=None,
        bysetpos=None,
        count=None,
        until_date=None,
        deleted=None,
        title=None,
        invite_message=None,
    ) -> dict[str, Any]:
        """
        Creates a new subscription for a project using the provided project ID and returns a successful creation status.

        Args:
            project_id (string): project_id
            id (integer): id
            target_type (string): * `email` - Email
        * `slack` - Slack
        * `webhook` - Webhook
            target_value (string): target_value
            frequency (string): * `daily` - Daily
        * `weekly` - Weekly
        * `monthly` - Monthly
        * `yearly` - Yearly
            start_date (string): start_date
            created_at (string): created_at
            created_by (string): created_by
            summary (string): summary
            next_delivery_date (string): next_delivery_date
            dashboard (integer): dashboard
            insight (integer): insight
            interval (integer): interval
            byweekday (array): byweekday
            bysetpos (integer): bysetpos
            count (integer): count
            until_date (string): until_date
            deleted (boolean): deleted
            title (string): title
            invite_message (string): invite_message

        Returns:
            dict[str, Any]: API response data.

        Tags:
            subscriptions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "dashboard": dashboard,
            "insight": insight,
            "target_type": target_type,
            "target_value": target_value,
            "frequency": frequency,
            "interval": interval,
            "byweekday": byweekday,
            "bysetpos": bysetpos,
            "count": count,
            "start_date": start_date,
            "until_date": until_date,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "title": title,
            "summary": summary,
            "next_delivery_date": next_delivery_date,
            "invite_message": invite_message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/subscriptions/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_retrieve(self, project_id, id) -> dict[str, Any]:
        """
        Retrieves details about a specific subscription within a project.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            subscriptions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/subscriptions/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_update(
        self,
        project_id,
        id,
        id_body,
        target_type,
        target_value,
        frequency,
        start_date,
        created_at,
        created_by,
        summary,
        next_delivery_date,
        dashboard=None,
        insight=None,
        interval=None,
        byweekday=None,
        bysetpos=None,
        count=None,
        until_date=None,
        deleted=None,
        title=None,
        invite_message=None,
    ) -> dict[str, Any]:
        """
        Updates an existing subscription associated with a specific project by replacing it with the provided data.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (integer): id
            target_type (string): * `email` - Email
        * `slack` - Slack
        * `webhook` - Webhook
            target_value (string): target_value
            frequency (string): * `daily` - Daily
        * `weekly` - Weekly
        * `monthly` - Monthly
        * `yearly` - Yearly
            start_date (string): start_date
            created_at (string): created_at
            created_by (string): created_by
            summary (string): summary
            next_delivery_date (string): next_delivery_date
            dashboard (integer): dashboard
            insight (integer): insight
            interval (integer): interval
            byweekday (array): byweekday
            bysetpos (integer): bysetpos
            count (integer): count
            until_date (string): until_date
            deleted (boolean): deleted
            title (string): title
            invite_message (string): invite_message

        Returns:
            dict[str, Any]: API response data.

        Tags:
            subscriptions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "dashboard": dashboard,
            "insight": insight,
            "target_type": target_type,
            "target_value": target_value,
            "frequency": frequency,
            "interval": interval,
            "byweekday": byweekday,
            "bysetpos": bysetpos,
            "count": count,
            "start_date": start_date,
            "until_date": until_date,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "title": title,
            "summary": summary,
            "next_delivery_date": next_delivery_date,
            "invite_message": invite_message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/subscriptions/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_partial_update(
        self,
        project_id,
        id,
        id_body=None,
        dashboard=None,
        insight=None,
        target_type=None,
        target_value=None,
        frequency=None,
        interval=None,
        byweekday=None,
        bysetpos=None,
        count=None,
        start_date=None,
        until_date=None,
        created_at=None,
        created_by=None,
        deleted=None,
        title=None,
        summary=None,
        next_delivery_date=None,
        invite_message=None,
    ) -> dict[str, Any]:
        """
        Updates a subscription by partially modifying its properties, such as specified fields, using the "/api/projects/{project_id}/subscriptions/{id}/" endpoint with the PATCH method.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (integer): id
            dashboard (integer): dashboard
            insight (integer): insight
            target_type (string): * `email` - Email
        * `slack` - Slack
        * `webhook` - Webhook
            target_value (string): target_value
            frequency (string): * `daily` - Daily
        * `weekly` - Weekly
        * `monthly` - Monthly
        * `yearly` - Yearly
            interval (integer): interval
            byweekday (array): byweekday
            bysetpos (integer): bysetpos
            count (integer): count
            start_date (string): start_date
            until_date (string): until_date
            created_at (string): created_at
            created_by (string): created_by
            deleted (boolean): deleted
            title (string): title
            summary (string): summary
            next_delivery_date (string): next_delivery_date
            invite_message (string): invite_message

        Returns:
            dict[str, Any]: API response data.

        Tags:
            subscriptions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "dashboard": dashboard,
            "insight": insight,
            "target_type": target_type,
            "target_value": target_value,
            "frequency": frequency,
            "interval": interval,
            "byweekday": byweekday,
            "bysetpos": bysetpos,
            "count": count,
            "start_date": start_date,
            "until_date": until_date,
            "created_at": created_at,
            "created_by": created_by,
            "deleted": deleted,
            "title": title,
            "summary": summary,
            "next_delivery_date": next_delivery_date,
            "invite_message": invite_message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/subscriptions/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscriptions_destroy(self, project_id, id) -> Any:
        """
        Deletes a specific subscription associated with a project by its identifier.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: API response data.

        Tags:
            subscriptions
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/subscriptions/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_list(
        self, project_id, limit=None, offset=None, search=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of surveys for a specific project with optional search and pagination parameters.

        Args:
            project_id (string): project_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.
            search (string): A search term.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            surveys, important
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/"
        query_params = {
            k: v
            for k, v in [("limit", limit), ("offset", offset), ("search", search)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_create(
        self,
        project_id,
        id,
        name,
        type,
        linked_flag,
        targeting_flag,
        internal_targeting_flag,
        created_at,
        created_by,
        description=None,
        schedule=None,
        linked_flag_id=None,
        targeting_flag_id=None,
        targeting_flag_filters=None,
        remove_targeting_flag=None,
        questions=None,
        conditions=None,
        appearance=None,
        start_date=None,
        end_date=None,
        archived=None,
        responses_limit=None,
        iteration_count=None,
        iteration_frequency_days=None,
        iteration_start_dates=None,
        current_iteration=None,
        current_iteration_start_date=None,
        response_sampling_start_date=None,
        response_sampling_interval_type=None,
        response_sampling_interval=None,
        response_sampling_limit=None,
        response_sampling_daily_limits=None,
        enable_partial_responses=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Creates a new survey under the specified project and returns a status message upon successful creation.

        Args:
            project_id (string): project_id
            id (string): id
            name (string): name
            type (string): * `popover` - popover
        * `widget` - widget
        * `button` - button
        * `email` - email
        * `full_screen` - full screen
        * `api` - api
            linked_flag (string): linked_flag
            targeting_flag (string): targeting_flag
            internal_targeting_flag (string): internal_targeting_flag
            created_at (string): created_at
            created_by (string): created_by
            description (string): description
            schedule (string): schedule
            linked_flag_id (integer): linked_flag_id
            targeting_flag_id (integer): targeting_flag_id
            targeting_flag_filters (string): targeting_flag_filters
            remove_targeting_flag (boolean): remove_targeting_flag
            questions (string):
                The `array` of questions included in the survey. Each question must conform to one of the defined question types: Basic, Link, Rating, or Multiple Choice.

                Basic (open-ended question)
                - `type`: `open`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `branching`: Branching logic for the question. See branching types below for details.

                Link (a question with a link)
                - `type`: `link`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `link`: The URL associated with the question.
                - `branching`: Branching logic for the question. See branching types below for details.

                Rating (a question with a rating scale)
                - `type`: `rating`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `display`: Display style of the rating (`number` or `emoji`).
                - `scale`: The scale of the rating (`number`).
                - `lowerBoundLabel`: Label for the lower bound of the scale.
                - `upperBoundLabel`: Label for the upper bound of the scale.
                - `branching`: Branching logic for the question. See branching types below for details.

                Multiple choice
                - `type`: `single_choice` or `multiple_choice`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `choices`: An array of choices for the question.
                - `shuffleOptions`: Whether to shuffle the order of the choices (`boolean`).
                - `hasOpenChoice`: Whether the question allows an open-ended response (`boolean`).
                - `branching`: Branching logic for the question. See branching types below for details.

                Branching logic can be one of the following types:

                Next question: Proceeds to the next question
                ```json
                {
                    "type": "next_question"
                }
                ```

                End: Ends the survey, optionally displaying a confirmation message.
                ```json
                {
                    "type": "end"
                }
                ```

                Response-based: Branches based on the response values. Available for the `rating` and `single_choice` question types.
                ```json
                {
                    "type": "response_based",
                    "responseValues": {
                        "responseKey": "value"
                    }
                }
                ```

                Specific question: Proceeds to a specific question by index.
                ```json
                {
                    "type": "specific_question",
                    "index": 2
                }
                ```

            conditions (string): conditions
            appearance (string): appearance
            start_date (string): start_date
            end_date (string): end_date
            archived (boolean): archived
            responses_limit (integer): responses_limit
            iteration_count (integer): iteration_count
            iteration_frequency_days (integer): iteration_frequency_days
            iteration_start_dates (array): iteration_start_dates
            current_iteration (integer): current_iteration
            current_iteration_start_date (string): current_iteration_start_date
            response_sampling_start_date (string): response_sampling_start_date
            response_sampling_interval_type (string): response_sampling_interval_type
            response_sampling_interval (integer): response_sampling_interval
            response_sampling_limit (integer): response_sampling_limit
            response_sampling_daily_limits (string): response_sampling_daily_limits
            enable_partial_responses (boolean): enable_partial_responses
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            surveys, important
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "description": description,
            "type": type,
            "schedule": schedule,
            "linked_flag": linked_flag,
            "linked_flag_id": linked_flag_id,
            "targeting_flag_id": targeting_flag_id,
            "targeting_flag": targeting_flag,
            "internal_targeting_flag": internal_targeting_flag,
            "targeting_flag_filters": targeting_flag_filters,
            "remove_targeting_flag": remove_targeting_flag,
            "questions": questions,
            "conditions": conditions,
            "appearance": appearance,
            "created_at": created_at,
            "created_by": created_by,
            "start_date": start_date,
            "end_date": end_date,
            "archived": archived,
            "responses_limit": responses_limit,
            "iteration_count": iteration_count,
            "iteration_frequency_days": iteration_frequency_days,
            "iteration_start_dates": iteration_start_dates,
            "current_iteration": current_iteration,
            "current_iteration_start_date": current_iteration_start_date,
            "response_sampling_start_date": response_sampling_start_date,
            "response_sampling_interval_type": response_sampling_interval_type,
            "response_sampling_interval": response_sampling_interval,
            "response_sampling_limit": response_sampling_limit,
            "response_sampling_daily_limits": response_sampling_daily_limits,
            "enable_partial_responses": enable_partial_responses,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/surveys/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_retrieve(self, project_id, id) -> dict[str, Any]:
        """
        Retrieves details for a specific survey in a project using the provided ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_update(
        self,
        project_id,
        id,
        id_body,
        name,
        type,
        linked_flag,
        targeting_flag,
        internal_targeting_flag,
        conditions,
        created_at,
        created_by,
        feature_flag_keys,
        description=None,
        schedule=None,
        linked_flag_id=None,
        questions=None,
        appearance=None,
        start_date=None,
        end_date=None,
        archived=None,
        responses_limit=None,
        iteration_count=None,
        iteration_frequency_days=None,
        iteration_start_dates=None,
        current_iteration=None,
        current_iteration_start_date=None,
        response_sampling_start_date=None,
        response_sampling_interval_type=None,
        response_sampling_interval=None,
        response_sampling_limit=None,
        response_sampling_daily_limits=None,
        enable_partial_responses=None,
    ) -> dict[str, Any]:
        """
        Updates a survey specified by its ID within a project identified by its ID using the PUT method.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            name (string): name
            type (string): * `popover` - popover
        * `widget` - widget
        * `button` - button
        * `email` - email
        * `full_screen` - full screen
        * `api` - api
            linked_flag (string): linked_flag
            targeting_flag (string): targeting_flag
            internal_targeting_flag (string): internal_targeting_flag
            conditions (string): conditions
            created_at (string): created_at
            created_by (string): created_by
            feature_flag_keys (array): feature_flag_keys
            description (string): description
            schedule (string): schedule
            linked_flag_id (integer): linked_flag_id
            questions (string):
                The `array` of questions included in the survey. Each question must conform to one of the defined question types: Basic, Link, Rating, or Multiple Choice.

                Basic (open-ended question)
                - `type`: `open`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `branching`: Branching logic for the question. See branching types below for details.

                Link (a question with a link)
                - `type`: `link`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `link`: The URL associated with the question.
                - `branching`: Branching logic for the question. See branching types below for details.

                Rating (a question with a rating scale)
                - `type`: `rating`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `display`: Display style of the rating (`number` or `emoji`).
                - `scale`: The scale of the rating (`number`).
                - `lowerBoundLabel`: Label for the lower bound of the scale.
                - `upperBoundLabel`: Label for the upper bound of the scale.
                - `branching`: Branching logic for the question. See branching types below for details.

                Multiple choice
                - `type`: `single_choice` or `multiple_choice`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `choices`: An array of choices for the question.
                - `shuffleOptions`: Whether to shuffle the order of the choices (`boolean`).
                - `hasOpenChoice`: Whether the question allows an open-ended response (`boolean`).
                - `branching`: Branching logic for the question. See branching types below for details.

                Branching logic can be one of the following types:

                Next question: Proceeds to the next question
                ```json
                {
                    "type": "next_question"
                }
                ```

                End: Ends the survey, optionally displaying a confirmation message.
                ```json
                {
                    "type": "end"
                }
                ```

                Response-based: Branches based on the response values. Available for the `rating` and `single_choice` question types.
                ```json
                {
                    "type": "response_based",
                    "responseValues": {
                        "responseKey": "value"
                    }
                }
                ```

                Specific question: Proceeds to a specific question by index.
                ```json
                {
                    "type": "specific_question",
                    "index": 2
                }
                ```

            appearance (string): appearance
            start_date (string): start_date
            end_date (string): end_date
            archived (boolean): archived
            responses_limit (integer): responses_limit
            iteration_count (integer): iteration_count
            iteration_frequency_days (integer): iteration_frequency_days
            iteration_start_dates (array): iteration_start_dates
            current_iteration (integer): current_iteration
            current_iteration_start_date (string): current_iteration_start_date
            response_sampling_start_date (string): response_sampling_start_date
            response_sampling_interval_type (string): response_sampling_interval_type
            response_sampling_interval (integer): response_sampling_interval
            response_sampling_limit (integer): response_sampling_limit
            response_sampling_daily_limits (string): response_sampling_daily_limits
            enable_partial_responses (boolean): enable_partial_responses

        Returns:
            dict[str, Any]: API response data.

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "description": description,
            "type": type,
            "schedule": schedule,
            "linked_flag": linked_flag,
            "linked_flag_id": linked_flag_id,
            "targeting_flag": targeting_flag,
            "internal_targeting_flag": internal_targeting_flag,
            "questions": questions,
            "conditions": conditions,
            "appearance": appearance,
            "created_at": created_at,
            "created_by": created_by,
            "start_date": start_date,
            "end_date": end_date,
            "archived": archived,
            "responses_limit": responses_limit,
            "feature_flag_keys": feature_flag_keys,
            "iteration_count": iteration_count,
            "iteration_frequency_days": iteration_frequency_days,
            "iteration_start_dates": iteration_start_dates,
            "current_iteration": current_iteration,
            "current_iteration_start_date": current_iteration_start_date,
            "response_sampling_start_date": response_sampling_start_date,
            "response_sampling_interval_type": response_sampling_interval_type,
            "response_sampling_interval": response_sampling_interval,
            "response_sampling_limit": response_sampling_limit,
            "response_sampling_daily_limits": response_sampling_daily_limits,
            "enable_partial_responses": enable_partial_responses,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_partial_update(
        self,
        project_id,
        id,
        id_body=None,
        name=None,
        description=None,
        type=None,
        schedule=None,
        linked_flag=None,
        linked_flag_id=None,
        targeting_flag_id=None,
        targeting_flag=None,
        internal_targeting_flag=None,
        targeting_flag_filters=None,
        remove_targeting_flag=None,
        questions=None,
        conditions=None,
        appearance=None,
        created_at=None,
        created_by=None,
        start_date=None,
        end_date=None,
        archived=None,
        responses_limit=None,
        iteration_count=None,
        iteration_frequency_days=None,
        iteration_start_dates=None,
        current_iteration=None,
        current_iteration_start_date=None,
        response_sampling_start_date=None,
        response_sampling_interval_type=None,
        response_sampling_interval=None,
        response_sampling_limit=None,
        response_sampling_daily_limits=None,
        enable_partial_responses=None,
        create_in_folder=None,
    ) -> dict[str, Any]:
        """
        Updates a specific survey within a project by applying partial modifications and returns a success status.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            name (string): name
            description (string): description
            type (string): * `popover` - popover
        * `widget` - widget
        * `button` - button
        * `email` - email
        * `full_screen` - full screen
        * `api` - api
            schedule (string): schedule
            linked_flag (string): linked_flag
            linked_flag_id (integer): linked_flag_id
            targeting_flag_id (integer): targeting_flag_id
            targeting_flag (string): targeting_flag
            internal_targeting_flag (string): internal_targeting_flag
            targeting_flag_filters (string): targeting_flag_filters
            remove_targeting_flag (boolean): remove_targeting_flag
            questions (string):
                The `array` of questions included in the survey. Each question must conform to one of the defined question types: Basic, Link, Rating, or Multiple Choice.

                Basic (open-ended question)
                - `type`: `open`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `branching`: Branching logic for the question. See branching types below for details.

                Link (a question with a link)
                - `type`: `link`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `link`: The URL associated with the question.
                - `branching`: Branching logic for the question. See branching types below for details.

                Rating (a question with a rating scale)
                - `type`: `rating`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `display`: Display style of the rating (`number` or `emoji`).
                - `scale`: The scale of the rating (`number`).
                - `lowerBoundLabel`: Label for the lower bound of the scale.
                - `upperBoundLabel`: Label for the upper bound of the scale.
                - `branching`: Branching logic for the question. See branching types below for details.

                Multiple choice
                - `type`: `single_choice` or `multiple_choice`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `choices`: An array of choices for the question.
                - `shuffleOptions`: Whether to shuffle the order of the choices (`boolean`).
                - `hasOpenChoice`: Whether the question allows an open-ended response (`boolean`).
                - `branching`: Branching logic for the question. See branching types below for details.

                Branching logic can be one of the following types:

                Next question: Proceeds to the next question
                ```json
                {
                    "type": "next_question"
                }
                ```

                End: Ends the survey, optionally displaying a confirmation message.
                ```json
                {
                    "type": "end"
                }
                ```

                Response-based: Branches based on the response values. Available for the `rating` and `single_choice` question types.
                ```json
                {
                    "type": "response_based",
                    "responseValues": {
                        "responseKey": "value"
                    }
                }
                ```

                Specific question: Proceeds to a specific question by index.
                ```json
                {
                    "type": "specific_question",
                    "index": 2
                }
                ```

            conditions (string): conditions
            appearance (string): appearance
            created_at (string): created_at
            created_by (string): created_by
            start_date (string): start_date
            end_date (string): end_date
            archived (boolean): archived
            responses_limit (integer): responses_limit
            iteration_count (integer): iteration_count
            iteration_frequency_days (integer): iteration_frequency_days
            iteration_start_dates (array): iteration_start_dates
            current_iteration (integer): current_iteration
            current_iteration_start_date (string): current_iteration_start_date
            response_sampling_start_date (string): response_sampling_start_date
            response_sampling_interval_type (string): response_sampling_interval_type
            response_sampling_interval (integer): response_sampling_interval
            response_sampling_limit (integer): response_sampling_limit
            response_sampling_daily_limits (string): response_sampling_daily_limits
            enable_partial_responses (boolean): enable_partial_responses
            create_in_folder (string): _create_in_folder

        Returns:
            dict[str, Any]: API response data.

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "description": description,
            "type": type,
            "schedule": schedule,
            "linked_flag": linked_flag,
            "linked_flag_id": linked_flag_id,
            "targeting_flag_id": targeting_flag_id,
            "targeting_flag": targeting_flag,
            "internal_targeting_flag": internal_targeting_flag,
            "targeting_flag_filters": targeting_flag_filters,
            "remove_targeting_flag": remove_targeting_flag,
            "questions": questions,
            "conditions": conditions,
            "appearance": appearance,
            "created_at": created_at,
            "created_by": created_by,
            "start_date": start_date,
            "end_date": end_date,
            "archived": archived,
            "responses_limit": responses_limit,
            "iteration_count": iteration_count,
            "iteration_frequency_days": iteration_frequency_days,
            "iteration_start_dates": iteration_start_dates,
            "current_iteration": current_iteration,
            "current_iteration_start_date": current_iteration_start_date,
            "response_sampling_start_date": response_sampling_start_date,
            "response_sampling_interval_type": response_sampling_interval_type,
            "response_sampling_interval": response_sampling_interval,
            "response_sampling_limit": response_sampling_limit,
            "response_sampling_daily_limits": response_sampling_daily_limits,
            "enable_partial_responses": enable_partial_responses,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_destroy(self, project_id, id) -> Any:
        """
        Deletes a survey identified by `{id}` within a project specified by `{project_id}` using the HTTP DELETE method.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_activity_retrieve_2(self, project_id, id) -> Any:
        """
        Retrieves the activity details for a specific survey within a project.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/activity/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_stats_retrieve_2(self, project_id, id) -> Any:
        """
        Retrieves aggregated response statistics for a specific survey within a project.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/stats/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_summarize_responses_create(
        self,
        project_id,
        id,
        id_body,
        name,
        type,
        linked_flag,
        targeting_flag,
        internal_targeting_flag,
        created_at,
        created_by,
        description=None,
        schedule=None,
        linked_flag_id=None,
        targeting_flag_id=None,
        targeting_flag_filters=None,
        remove_targeting_flag=None,
        questions=None,
        conditions=None,
        appearance=None,
        start_date=None,
        end_date=None,
        archived=None,
        responses_limit=None,
        iteration_count=None,
        iteration_frequency_days=None,
        iteration_start_dates=None,
        current_iteration=None,
        current_iteration_start_date=None,
        response_sampling_start_date=None,
        response_sampling_interval_type=None,
        response_sampling_interval=None,
        response_sampling_limit=None,
        response_sampling_daily_limits=None,
        enable_partial_responses=None,
        create_in_folder=None,
    ) -> Any:
        """
        Generates summarized insights from survey responses for a specified project and survey using AI-powered summarization.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (string): id
            name (string): name
            type (string): * `popover` - popover
        * `widget` - widget
        * `button` - button
        * `email` - email
        * `full_screen` - full screen
        * `api` - api
            linked_flag (string): linked_flag
            targeting_flag (string): targeting_flag
            internal_targeting_flag (string): internal_targeting_flag
            created_at (string): created_at
            created_by (string): created_by
            description (string): description
            schedule (string): schedule
            linked_flag_id (integer): linked_flag_id
            targeting_flag_id (integer): targeting_flag_id
            targeting_flag_filters (string): targeting_flag_filters
            remove_targeting_flag (boolean): remove_targeting_flag
            questions (string):
                The `array` of questions included in the survey. Each question must conform to one of the defined question types: Basic, Link, Rating, or Multiple Choice.

                Basic (open-ended question)
                - `type`: `open`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `branching`: Branching logic for the question. See branching types below for details.

                Link (a question with a link)
                - `type`: `link`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `link`: The URL associated with the question.
                - `branching`: Branching logic for the question. See branching types below for details.

                Rating (a question with a rating scale)
                - `type`: `rating`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `display`: Display style of the rating (`number` or `emoji`).
                - `scale`: The scale of the rating (`number`).
                - `lowerBoundLabel`: Label for the lower bound of the scale.
                - `upperBoundLabel`: Label for the upper bound of the scale.
                - `branching`: Branching logic for the question. See branching types below for details.

                Multiple choice
                - `type`: `single_choice` or `multiple_choice`
                - `question`: The text of the question.
                - `description`: Optional description of the question.
                - `descriptionContentType`: Content type of the description (`html` or `text`).
                - `optional`: Whether the question is optional (`boolean`).
                - `buttonText`: Text displayed on the submit button.
                - `choices`: An array of choices for the question.
                - `shuffleOptions`: Whether to shuffle the order of the choices (`boolean`).
                - `hasOpenChoice`: Whether the question allows an open-ended response (`boolean`).
                - `branching`: Branching logic for the question. See branching types below for details.

                Branching logic can be one of the following types:

                Next question: Proceeds to the next question
                ```json
                {
                    "type": "next_question"
                }
                ```

                End: Ends the survey, optionally displaying a confirmation message.
                ```json
                {
                    "type": "end"
                }
                ```

                Response-based: Branches based on the response values. Available for the `rating` and `single_choice` question types.
                ```json
                {
                    "type": "response_based",
                    "responseValues": {
                        "responseKey": "value"
                    }
                }
                ```

                Specific question: Proceeds to a specific question by index.
                ```json
                {
                    "type": "specific_question",
                    "index": 2
                }
                ```

            conditions (string): conditions
            appearance (string): appearance
            start_date (string): start_date
            end_date (string): end_date
            archived (boolean): archived
            responses_limit (integer): responses_limit
            iteration_count (integer): iteration_count
            iteration_frequency_days (integer): iteration_frequency_days
            iteration_start_dates (array): iteration_start_dates
            current_iteration (integer): current_iteration
            current_iteration_start_date (string): current_iteration_start_date
            response_sampling_start_date (string): response_sampling_start_date
            response_sampling_interval_type (string): response_sampling_interval_type
            response_sampling_interval (integer): response_sampling_interval
            response_sampling_limit (integer): response_sampling_limit
            response_sampling_daily_limits (string): response_sampling_daily_limits
            enable_partial_responses (boolean): enable_partial_responses
            create_in_folder (string): _create_in_folder

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "description": description,
            "type": type,
            "schedule": schedule,
            "linked_flag": linked_flag,
            "linked_flag_id": linked_flag_id,
            "targeting_flag_id": targeting_flag_id,
            "targeting_flag": targeting_flag,
            "internal_targeting_flag": internal_targeting_flag,
            "targeting_flag_filters": targeting_flag_filters,
            "remove_targeting_flag": remove_targeting_flag,
            "questions": questions,
            "conditions": conditions,
            "appearance": appearance,
            "created_at": created_at,
            "created_by": created_by,
            "start_date": start_date,
            "end_date": end_date,
            "archived": archived,
            "responses_limit": responses_limit,
            "iteration_count": iteration_count,
            "iteration_frequency_days": iteration_frequency_days,
            "iteration_start_dates": iteration_start_dates,
            "current_iteration": current_iteration,
            "current_iteration_start_date": current_iteration_start_date,
            "response_sampling_start_date": response_sampling_start_date,
            "response_sampling_interval_type": response_sampling_interval_type,
            "response_sampling_interval": response_sampling_interval,
            "response_sampling_limit": response_sampling_limit,
            "response_sampling_daily_limits": response_sampling_daily_limits,
            "enable_partial_responses": enable_partial_responses,
            "_create_in_folder": create_in_folder,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/surveys/{id}/summarize_responses/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_activity_retrieve(self, project_id) -> Any:
        """
        Retrieves activity data for surveys associated with a specific project ID.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/activity/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_responses_count_retrieve(self, project_id) -> Any:
        """
        Retrieves the count of survey responses for a specified project using the project ID.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/responses_count/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def surveys_stats_retrieve(self, project_id) -> Any:
        """
        Retrieves aggregated response statistics across all surveys for a specified project, providing total counts and rates, using the "GET" method.

        Args:
            project_id (string): project_id

        Returns:
            Any: No response body

        Tags:
            surveys
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/surveys/stats/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def web_experiments_list(
        self, project_id, limit=None, offset=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of web experiments for a specified project using the Optimizely Web Experimentation API, allowing for pagination via optional limit and offset parameters.

        Args:
            project_id (string): project_id
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            web_experiments
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        url = f"{self.base_url}/api/projects/{project_id}/web_experiments/"
        query_params = {
            k: v for k, v in [("limit", limit), ("offset", offset)] if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def web_experiments_create(
        self, project_id, id, name, feature_flag_key, created_at=None, variants=None
    ) -> dict[str, Any]:
        """
        Creates a new web experiment within a specified project using the Optimizely Web Experimentation API and returns a successful creation status message.

        Args:
            project_id (string): project_id
            id (integer): id
            name (string): name
            feature_flag_key (string): feature_flag_key
            created_at (string): created_at
            variants (string): variants

        Returns:
            dict[str, Any]: API response data.

        Tags:
            web_experiments
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        request_body = {
            "id": id,
            "name": name,
            "created_at": created_at,
            "feature_flag_key": feature_flag_key,
            "variants": variants,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/web_experiments/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def web_experiments_retrieve(self, project_id, id) -> dict[str, Any]:
        """
        Retrieves details about a specific web experiment defined by its ID within a specified project using the Optimizely Web Experimentation API.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            dict[str, Any]: API response data.

        Tags:
            web_experiments
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/web_experiments/{id}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def web_experiments_update(
        self,
        project_id,
        id,
        id_body,
        name,
        feature_flag_key,
        created_at=None,
        variants=None,
    ) -> dict[str, Any]:
        """
        Updates a web experiment for a specified project using the provided ID and returns a success status upon completion.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (integer): id
            name (string): name
            feature_flag_key (string): feature_flag_key
            created_at (string): created_at
            variants (string): variants

        Returns:
            dict[str, Any]: API response data.

        Tags:
            web_experiments
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "created_at": created_at,
            "feature_flag_key": feature_flag_key,
            "variants": variants,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/web_experiments/{id}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def web_experiments_partial_update(
        self,
        project_id,
        id,
        id_body=None,
        name=None,
        created_at=None,
        feature_flag_key=None,
        variants=None,
    ) -> dict[str, Any]:
        """
        Updates specific properties of a web experiment in a project using the PATCH method, returning a successful response upon modification.

        Args:
            project_id (string): project_id
            id (string): id
            id_body (integer): id
            name (string): name
            created_at (string): created_at
            feature_flag_key (string): feature_flag_key
            variants (string): variants

        Returns:
            dict[str, Any]: API response data.

        Tags:
            web_experiments
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        request_body = {
            "id": id_body,
            "name": name,
            "created_at": created_at,
            "feature_flag_key": feature_flag_key,
            "variants": variants,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/projects/{project_id}/web_experiments/{id}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def web_experiments_destroy(self, project_id, id) -> Any:
        """
        Deletes a web experiment associated with a specified project using the project ID and experiment ID.

        Args:
            project_id (string): project_id
            id (string): id

        Returns:
            Any: No response body

        Tags:
            web_experiments
        """
        if project_id is None:
            raise ValueError("Missing required parameter 'project_id'")
        if id is None:
            raise ValueError("Missing required parameter 'id'")
        url = f"{self.base_url}/api/projects/{project_id}/web_experiments/{id}/"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_list(self, is_staff=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a list of user records from the system, filtered by staff status, with optional pagination using limit and offset parameters.

        Args:
            is_staff (boolean): `is_staff` indicates whether to filter users by staff status (true/false).
            limit (integer): Number of results to return per page.
            offset (integer): The initial index from which to return the results.

        Returns:
            dict[str, Any]: API response data.

        Tags:
            users, users
        """
        url = f"{self.base_url}/api/users/"
        query_params = {
            k: v
            for k, v in [("is_staff", is_staff), ("limit", limit), ("offset", offset)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_retrieve(self, uuid) -> dict[str, Any]:
        """
        Retrieves user data for a specific user identified by the provided UUID using the GET method.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: API response data.

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/api/users/{uuid}/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_update(
        self,
        uuid,
        date_joined,
        uuid_body,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> dict[str, Any]:
        """
        Updates or replaces a user's entire resource at the specified UUID endpoint using the provided data.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            dict[str, Any]: API response data.

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_partial_update(
        self,
        uuid,
        date_joined=None,
        uuid_body=None,
        distinct_id=None,
        first_name=None,
        last_name=None,
        email=None,
        pending_email=None,
        is_email_verified=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        has_password=None,
        is_staff=None,
        is_impersonated=None,
        is_impersonated_until=None,
        sensitive_session_expires_at=None,
        team=None,
        organization=None,
        organizations=None,
        set_current_organization=None,
        set_current_team=None,
        password=None,
        current_password=None,
        events_column_config=None,
        is_2fa_enabled=None,
        has_social_auth=None,
        has_seen_product_intro_for=None,
        scene_personalisation=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> dict[str, Any]:
        """
        Updates a specific user's details, identified by their UUID, using partial modifications via the PATCH method.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            first_name (string): first_name
            last_name (string): last_name
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            has_password (boolean): has_password
            is_staff (boolean): Designates whether the user can log into this admin site.
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            password (string): password
            current_password (string): current_password
            events_column_config (string): events_column_config
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            has_seen_product_intro_for (string): has_seen_product_intro_for
            scene_personalisation (array): scene_personalisation
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            dict[str, Any]: API response data.

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_hedgehog_config_retrieve(self, uuid) -> Any:
        """
        Retrieves the hedgehog configuration for a user identified by the specified UUID.

        Args:
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/api/users/{uuid}/hedgehog_config/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_hedgehog_config_partial_update(
        self,
        uuid,
        date_joined=None,
        uuid_body=None,
        distinct_id=None,
        first_name=None,
        last_name=None,
        email=None,
        pending_email=None,
        is_email_verified=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        has_password=None,
        is_staff=None,
        is_impersonated=None,
        is_impersonated_until=None,
        sensitive_session_expires_at=None,
        team=None,
        organization=None,
        organizations=None,
        set_current_organization=None,
        set_current_team=None,
        password=None,
        current_password=None,
        events_column_config=None,
        is_2fa_enabled=None,
        has_social_auth=None,
        has_seen_product_intro_for=None,
        scene_personalisation=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Updates the hedgehog configuration settings for a specific user identified by UUID using a PATCH request.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            first_name (string): first_name
            last_name (string): last_name
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            has_password (boolean): has_password
            is_staff (boolean): Designates whether the user can log into this admin site.
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            password (string): password
            current_password (string): current_password
            events_column_config (string): events_column_config
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            has_seen_product_intro_for (string): has_seen_product_intro_for
            scene_personalisation (array): scene_personalisation
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/hedgehog_config/"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_scene_personalisation_create(
        self,
        uuid,
        date_joined,
        uuid_body,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Sends a request to personalize a scene for a user identified by their UUID, enabling tailored experiences based on user-specific data.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/scene_personalisation/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_start_2fa_setup_retrieve(self, uuid) -> Any:
        """
        Starts the setup process for two-factor authentication (2FA) for a user identified by their UUID.

        Args:
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/api/users/{uuid}/start_2fa_setup/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_two_factor_backup_codes_create(
        self,
        uuid,
        date_joined,
        uuid_body,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Generates and stores backup codes for two-factor authentication (2FA) associated with the specified user UUID.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/two_factor_backup_codes/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_two_factor_disable_create(
        self,
        uuid,
        date_joined,
        uuid_body,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Disables two-factor authentication for a specific user identified by their UUID.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/two_factor_disable/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_two_factor_start_setup_retrieve(self, uuid) -> Any:
        """
        Initiates two-factor authentication setup for a user identified by their UUID, facilitating an additional security layer beyond the primary login credentials.

        Args:
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/api/users/{uuid}/two_factor_start_setup/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_two_factor_status_retrieve(self, uuid) -> Any:
        """
        Retrieves the two-factor authentication status for a user identified by the specified UUID using the GET method.

        Args:
            uuid (string): uuid

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/api/users/{uuid}/two_factor_status/"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_two_factor_validate_create(
        self,
        uuid,
        date_joined,
        uuid_body,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Validates two-factor authentication for a user identified by the provided UUID using the POST method.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/two_factor_validate/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_validate_2fa_create(
        self,
        uuid,
        date_joined,
        uuid_body,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Validates two-factor authentication for a user identified by the provided UUID using the API.

        Args:
            uuid (string): uuid
            date_joined (string): date_joined
            uuid_body (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid_body,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/{uuid}/validate_2fa/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_request_email_verification_create(
        self,
        date_joined,
        uuid,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Sends an email verification request to a user using the POST method at the path "/api/users/request_email_verification/".

        Args:
            date_joined (string): date_joined
            uuid (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/request_email_verification/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def users_verify_email_create(
        self,
        date_joined,
        uuid,
        distinct_id,
        email,
        pending_email,
        is_email_verified,
        has_password,
        is_impersonated,
        is_impersonated_until,
        sensitive_session_expires_at,
        team,
        organization,
        organizations,
        password,
        is_2fa_enabled,
        has_social_auth,
        scene_personalisation,
        first_name=None,
        last_name=None,
        notification_settings=None,
        anonymize_data=None,
        toolbar_mode=None,
        is_staff=None,
        set_current_organization=None,
        set_current_team=None,
        current_password=None,
        events_column_config=None,
        has_seen_product_intro_for=None,
        theme_mode=None,
        hedgehog_config=None,
        role_at_organization=None,
    ) -> Any:
        """
        Verifies an email address for a user using a POST request to the "/api/users/verify_email/" endpoint.

        Args:
            date_joined (string): date_joined
            uuid (string): uuid
            distinct_id (string): distinct_id
            email (string): email
            pending_email (string): pending_email
            is_email_verified (boolean): is_email_verified
            has_password (boolean): has_password
            is_impersonated (boolean): is_impersonated
            is_impersonated_until (string): is_impersonated_until
            sensitive_session_expires_at (string): sensitive_session_expires_at
            team (string): team
            organization (string): organization
            organizations (array): organizations
            password (string): password
            is_2fa_enabled (boolean): is_2fa_enabled
            has_social_auth (boolean): has_social_auth
            scene_personalisation (array): scene_personalisation
            first_name (string): first_name
            last_name (string): last_name
            notification_settings (object): notification_settings
            anonymize_data (boolean): anonymize_data
            toolbar_mode (string): toolbar_mode
            is_staff (boolean): Designates whether the user can log into this admin site.
            set_current_organization (string): set_current_organization
            set_current_team (string): set_current_team
            current_password (string): current_password
            events_column_config (string): events_column_config
            has_seen_product_intro_for (string): has_seen_product_intro_for
            theme_mode (string): theme_mode
            hedgehog_config (string): hedgehog_config
            role_at_organization (string): * `engineering` - Engineering
        * `data` - Data
        * `product` - Product Management
        * `founder` - Founder
        * `leadership` - Leadership
        * `marketing` - Marketing
        * `sales` - Sales / Success
        * `other` - Other

        Returns:
            Any: No response body

        Tags:
            users, users
        """
        request_body = {
            "date_joined": date_joined,
            "uuid": uuid,
            "distinct_id": distinct_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "pending_email": pending_email,
            "is_email_verified": is_email_verified,
            "notification_settings": notification_settings,
            "anonymize_data": anonymize_data,
            "toolbar_mode": toolbar_mode,
            "has_password": has_password,
            "is_staff": is_staff,
            "is_impersonated": is_impersonated,
            "is_impersonated_until": is_impersonated_until,
            "sensitive_session_expires_at": sensitive_session_expires_at,
            "team": team,
            "organization": organization,
            "organizations": organizations,
            "set_current_organization": set_current_organization,
            "set_current_team": set_current_team,
            "password": password,
            "current_password": current_password,
            "events_column_config": events_column_config,
            "is_2fa_enabled": is_2fa_enabled,
            "has_social_auth": has_social_auth,
            "has_seen_product_intro_for": has_seen_product_intro_for,
            "scene_personalisation": scene_personalisation,
            "theme_mode": theme_mode,
            "hedgehog_config": hedgehog_config,
            "role_at_organization": role_at_organization,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/api/users/verify_email/"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.is_generating_demo_data_retrieve,
            self.reset_token_partial_update,
            self.proxy_records_list,
            self.proxy_records_create,
            self.proxy_records_retrieve,
            self.proxy_records_update,
            self.proxy_records_partial_update,
            self.proxy_records_destroy,
            self.roles_list,
            self.roles_create,
            self.roles_retrieve,
            self.roles_update,
            self.roles_partial_update,
            self.roles_destroy,
            self.roles_role_memberships_list,
            self.roles_role_memberships_create,
            self.roles_role_memberships_destroy,
            self.actions_list,
            self.actions_create,
            self.notebooks_list,
            self.notebooks_create,
            self.notebooks_retrieve,
            self.notebooks_update,
            self.notebooks_partial_update,
            self.notebooks_destroy,
            self.notebooks_activity_retrieve_2,
            self.notebooks_activity_retrieve,
            self.notebooks_recording_comments_retrieve,
            self.persons_list,
            self.persons_retrieve,
            self.persons_update,
            self.persons_partial_update,
            self.persons_destroy,
            self.persons_activity_retrieve_2,
            self.persons_delete_events_create,
            self.persons_delete_property_create,
            self.persons_properties_timeline_retrieve,
            self.persons_split_create,
            self.persons_update_property_create,
            self.persons_activity_retrieve,
            self.persons_bulk_delete_create,
            self.persons_cohorts_retrieve,
            self.persons_funnel_retrieve,
            self.persons_funnel_create,
            self.persons_funnel_correlation_retrieve,
            self.persons_funnel_correlation_create,
            self.persons_lifecycle_retrieve,
            self.persons_reset_person_distinct_id_create,
            self.persons_stickiness_retrieve,
            self.persons_trends_retrieve,
            self.persons_values_retrieve,
            self.plugin_configs_logs_list,
            self.property_definitions_list,
            self.property_definitions_retrieve,
            self.property_definitions_update,
            self.property_definitions_partial_update,
            self.property_definitions_destroy,
            self.property_definitions_seen_together_retrieve,
            self.query_create,
            self.query_retrieve,
            self.query_destroy,
            self.query_check_auth_for_async_create,
            self.query_draft_sql_retrieve,
            self.session_recording_playlists_list,
            self.session_recording_playlists_create,
            self.session_recording_playlists_retrieve,
            self.session_recording_playlists_update,
            self.session_recording_playlists_partial_update,
            self.session_recording_playlists_destroy,
            self.session_recording_playlists_recordings_retrieve,
            self.session_recording_playlists_recordings_create,
            self.session_recording_playlists_recordings_destroy,
            self.session_recordings_list,
            self.session_recordings_retrieve,
            self.session_recordings_update,
            self.session_recordings_partial_update,
            self.session_recordings_destroy,
            self.session_recordings_analyze_similar_retrieve,
            self.session_recordings_sharing_list,
            self.session_recordings_ai_regex_create,
            self.sessions_property_definitions_retrieve,
            self.sessions_values_retrieve,
            self.subscriptions_list,
            self.subscriptions_create,
            self.subscriptions_retrieve,
            self.subscriptions_update,
            self.subscriptions_partial_update,
            self.subscriptions_destroy,
            self.surveys_list,
            self.surveys_create,
            self.surveys_retrieve,
            self.surveys_update,
            self.surveys_partial_update,
            self.surveys_destroy,
            self.surveys_activity_retrieve_2,
            self.surveys_stats_retrieve_2,
            self.surveys_summarize_responses_create,
            self.surveys_activity_retrieve,
            self.surveys_responses_count_retrieve,
            self.surveys_stats_retrieve,
            self.web_experiments_list,
            self.web_experiments_create,
            self.web_experiments_retrieve,
            self.web_experiments_update,
            self.web_experiments_partial_update,
            self.web_experiments_destroy,
            self.users_list,
            self.users_retrieve,
            self.users_update,
            self.users_partial_update,
            self.users_hedgehog_config_retrieve,
            self.users_hedgehog_config_partial_update,
            self.users_scene_personalisation_create,
            self.users_start_2fa_setup_retrieve,
            self.users_two_factor_backup_codes_create,
            self.users_two_factor_disable_create,
            self.users_two_factor_start_setup_retrieve,
            self.users_two_factor_status_retrieve,
            self.users_two_factor_validate_create,
            self.users_validate_2fa_create,
            self.users_request_email_verification_create,
            self.users_verify_email_create,
        ]
