"""
Meraki VLANs API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class VLANs(MerakiAPIResource):
    """ Meraki API Organization VLANs resource. """

    resource = "vlans"

    parameters = [
        "name"
        , "subnet"
        , "applianceIp"
        , "fixedIpAssignments"
        , "reservedIpRanges"
        , "vpnNatSubnet"
        , "vpnNatSubnet"
    ]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
