"""
Meraki Organizations API Resource
"""
import collections
from .meraki_api_resource import MerakiAPIResource
from .admins import Admins
from .networks import Networks
from .config_templates import ConfigTemplates
from .saml_roles import SAMLRoles
from .utils import clean


class Organizations(MerakiAPIResource):
    """ Meraki API Organizations resource. """

    resource = "organizations"

    parameters = ["name"]

    claim_parameters = ["order", "serial", "licenseKey", "licenseMode"]

    third_party_vpn_peers_parameters = [
        "name",
        "publicIp",
        "privateSubnets",
        "secret",
    ]

    def __init__(self, key, prefix=None, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def admins(self, admin_id=None):
        """ Returns the Organization Admins API Resource. """
        self.check_for_resource_id()
        return Admins(self.key, self.endpoint(), admin_id)

    def networks(self, network_id=None):
        """ Returns the Organization Networks API Resource. """
        self.check_for_resource_id()
        return Networks(self.key, self.endpoint(), network_id)

    def config_templates(self, config_template_id=None):
        """ Returns the Organization Config Templates API Resource. """
        self.check_for_resource_id()
        return ConfigTemplates(self.key, self.endpoint(), config_template_id)

    def saml_roles(self, saml_role_id=None):
        """ Returns the Organization SAML Roles API Resource. """
        self.check_for_resource_id()
        return SAMLRoles(self.key, self.endpoint(), saml_role_id)

    def clone(self, data):
        """ Create a new organization by cloning. """
        self.check_for_resource_id()
        data = clean(data, self.parameters)
        return self.post("/clone", data)

    def claim(self, data):
        """ Claim order, license key, or order into an organization. """
        self.check_for_resource_id()
        data = clean(data, self.claim_parameters)
        return self.post("/claim", data)

    def license_state(self):
        """ Return the license state. """
        self.check_for_resource_id()
        return self.get("/licenseState")

    def inventory(self):
        """ Return the license state. """
        self.check_for_resource_id()
        return self.get("/inventory")

    def snmp(self):
        """ Return the SNMP settings. """
        self.check_for_resource_id()
        return self.get("/snmp")

    def third_party_vpn_peers(self):
        """ Return the third party VPN peers. """
        self.check_for_resource_id()
        return self.get("/thirdPartyVPNPeers")

    def update_third_party_vpn_peers(self, data):
        """ Return the third party VPN peers. """
        self.check_for_resource_id()
        if not isinstance(data, collections.Iterable):
            raise ValueError("'data' must be a list")
        clean_data = []
        for item in data:
            clean_data.append(
                clean(item, self.third_party_vpn_peers_parameters)
            )
        return self.put("/thirdPartyVPNPeers", clean_data)
