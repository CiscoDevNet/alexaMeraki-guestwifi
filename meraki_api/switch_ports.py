"""
Meraki SwitchPorts API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class SwitchPorts(MerakiAPIResource):
    """ Meraki API Devices SwitchPorts resource. """

    resource = "switchPorts"

    parameters = [
        "name"
        , "tags"
        , "enabled"
        , "type"
        , "vlan"
        , "voiceVlan"
        , "allowedVlans"
        , "poeEnabled"
        , "isolationEnabled"
        , "rstpEnabled"
        , "stpGuard"
        , "accessPolicyNumber"
    ]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
