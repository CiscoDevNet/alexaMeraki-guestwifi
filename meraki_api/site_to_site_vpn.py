"""
Meraki Site-to-site VPN API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class SiteToSiteVPN(MerakiAPIResource):
    """ Meraki API Organization Admins resource. """

    resource = "siteToSiteVpn"

    parameters = ["mode", "hubs"]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
