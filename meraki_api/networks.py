"""
Meraki Networks API Resource
"""

import urllib
from .meraki_api_resource import MerakiAPIResource
from .devices import Devices
from .ssids import SSIDs
from .site_to_site_vpn import SiteToSiteVPN
from .phone_contacts import PhoneContacts
from .sm import SM
from .static_routes import StaticRoutes
from .vlans import VLANs
from .utils import clean


class Networks(MerakiAPIResource):
    """ Meraki API Networks resource. """

    resource = "networks"

    parameters = ["name", "timeZone", "tags", "type"]

    traffic_parameters = ["timespan", "deviceType"]

    air_marshal_parameters = ["timespan"]

    bind_parameters = ["configurationTemplateId", "autoBind"]

    def __init__(self, key, prefix=None, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def check_timespan(self, query):
        """ Checks if the query object has the timespan value configured. """
        if query is None or query.get("timespan") is None:
            raise ValueError("You must set the timespan query value.")

    def static_routes(self, static_route_id=None):
        """ Returns the Networks Static Routes API Resource. """
        self.check_for_resource_id()
        return StaticRoutes(self.key, self.endpoint(), static_route_id)

    def devices(self, serial=None):
        """ Returns the Networks Devices API Resource. """
        self.check_for_resource_id()
        return Devices(self.key, self.endpoint(), serial)

    def ssids(self, ssid_id=None):
        """ Returns the Network SSIDs API Resource."""
        self.check_for_resource_id()
        return SSIDs(self.key, self.endpoint(), ssid_id)

    def site_to_site_vpn(self, site_to_site_vpn_id=None):
        """ Returns site-to-site VPN settings API Resource. """
        self.check_for_resource_id()
        return SiteToSiteVPN(self.key, self.endpoint(), site_to_site_vpn_id)

    def vlans(self, vlan_id=None):
        """ Returns VLANs VPN settings API Resource. """
        self.check_for_resource_id()
        return VLANs(self.key, self.endpoint(), vlan_id)

    def sm(self):
        """ Returns Network SM API Resource. """
        self.check_for_resource_id()
        return SM(self.key, self.endpoint())

    def traffic(self, query):
        """
        The traffic analysis data for this network. Traffic Analysis with
        Hostname Visibility must be enabled on the network.
        """
        self.check_for_resource_id()
        self.check_timespan(query)
        query = clean(query, self.traffic_parameters)
        return self.get("/traffic?" + urllib.parse.urlencode(query))

    def bind(self, data):
        """ Binds template to network. """
        self.check_for_resource_id()
        data = clean(data, self.bind_parameters)
        return self.post("/bind", data)

    def unbind(self):
        """ Unbind template from network. """
        self.check_for_resource_id()
        return self.post("/unbind")

    def access_policies(self):
        """ List the access policies (MS). """
        self.check_for_resource_id()
        return self.get("/accessPolicies")

    def air_marshal(self, query):
        """ Air marshal scan results from a network. """
        self.check_timespan(query)
        self.check_for_resource_id()
        query = clean(query, self.air_marshal_parameters)
        return self.get("/airMarshal?" + urllib.parse.urlencode(query))

    def phone_contacts(self, phone_contact_id=None):
        """ List the phone contacts in a network. """
        self.check_for_resource_id()
        return PhoneContacts(self.key, self.endpoint(), phone_contact_id)

    def phone_numbers(self):
        """ List all the phone numbers in a network. """
        self.check_for_resource_id()
        return self.get("/phoneNumbers")

    def available_phone_numbers(self):
        """ List all the available phone numbers in a network. """
        self.check_for_resource_id()
        return self.get("/phoneNumbers/available")
