"""
Meraki SSIDs API Resource
"""

from .meraki_api_resource import MerakiAPIResource
from .l3_firewall_rules import L3FirewallRules


class SSIDs(MerakiAPIResource):
    """ Meraki API Organization Admins resource. """

    resource = "ssids"

    parameters = [
        "name"
        , "enabled"
        , "authMode"
        , "encriptionMode"
        , "psk"
        , "splashPage"
        , "radiusServer"
        , "radiusCoAEnabled"
        , "radiusAccountingEnabled"
        , "radiusAccountingServers"
        , "ipAssignmentMode"
        , "useVlanTagging"
        , "concentratorNetworkId"
        , "vlanId"
        , "defaultVlan"
        , "apTagsAndVlanIds"
        , "walledGardenEnabled"
        , "walledGardenRanges"
        , "minBitrate"
        , "bandSelection"
        , "perClientBandwidthLimitUp"
        , "perClientBandwidthLimitDown"
    ]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def l3_firewall_rules(self, l3_firewall_rule_id=None):
        """ Returns the L3 Firewall Rules API Resource. """
        return L3FirewallRules(self.key, self.endpoint(), l3_firewall_rule_id)
