"""
Meraki Devices API Resource
"""

import urllib
from .meraki_api_resource import MerakiAPIResource
from .switch_ports import SwitchPorts
from .utils import clean

class Devices(MerakiAPIResource):
    """ Meraki API Devices resource. """

    resource = "devices"

    parameters = ["name", "tags", "lat", "lng", "address", "moveMapMarker"]

    clients_parameters = ["timespan"]

    claim_parameters = ["serial"]

    def __init__(self, key, prefix=None, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def switch_ports(self, switch_port_id=None):
        """ Returns a Device Switch Ports API Resource. """
        self.check_for_resource_id()
        return SwitchPorts(self.key, self.endpoint(), switch_port_id)

    def clients(self, query):
        """
        List the clients of a device, up to a maximum of a month ago. The
        usage of each client is returned in kilobytes. If the device is a
        switch, the switchport is returned; otherwise the switchport field
        is null.
        """
        if query is None:
            raise ValueError("You must set the timespan query value.")
        query = clean(query, self.clients_parameters)
        return self.get("/clients?" + urllib.parse.urlencode(query))

    def uplink(self):
        """ Return uplink status. """
        if self.resource_id is None:
            raise ValueError("Cant't call this endpoint if the serial is not\
defined")
        return self.get("/uplink")

    def claim(self, query):
        """ Claim a device. """
        if self.resource_id is not None:
            raise ValueError("Can't claim a device already assigned.")
        if query is None or query.get("serial") is None:
            raise ValueError("Can't claim a device without its serial.")
        query = clean(query, self.claim_parameters)
        return self.post("/claim", query)

    def remove(self):
        """ Remove a single device. """
        if self.resource_id is None:
            raise ValueError("Can't remove a device without its serial.")
        return self.post("/remove")
