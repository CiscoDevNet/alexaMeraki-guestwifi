"""
Meraki Static Routes API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class StaticRoutes(MerakiAPIResource):
    """ Meraki API Network Staic Routes resource. """

    resource = "staticRoutes"

    parameters = [
        "name"
        , "subnet"
        , "gatewayIp"
        , "enabled"
        , "fixedIpAssignments"
        , "reservedIpRanges"
    ]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
