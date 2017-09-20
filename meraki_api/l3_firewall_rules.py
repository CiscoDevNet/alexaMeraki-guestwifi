"""
Meraki L3 Firewall Rules API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class L3FirewallRules(MerakiAPIResource):
    """ Meraki API L3 Firewall Rules resource. """

    resource = "l3FirewallRules"

    parameters = [
        "rules"
        , "comment"
        , "policy"
        , "protocol"
        , "destPort"
        , "destCidr"
        , "allowLanAccess"
    ]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
