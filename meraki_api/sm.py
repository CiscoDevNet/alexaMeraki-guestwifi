"""
Meraki SM API Resource
"""

import urllib
from .meraki_api_resource import MerakiAPIResource
from .utils import clean


class SM(MerakiAPIResource):
    """ Meraki API Network SM resource. """

    resource = "sm"

    devices_parameters = [
        "fields"
        , "wifiMacs"
        , "serials"
        , "ids"
        , "scope"
        , "batchToken"
    ]

    tags_parameters = [
        "wifiMacs"
        , "ids"
        , "serials"
        , "scope"
        , "pin"
        , "updateActions"
    ]

    fields_parameters = [
        "wifiMacs"
        , "id"
        , "serial"
        , "deviceFields"
    ]

    lock_parameters = [
        "wifiMacs"
        , "ids"
        , "serials"
        , "scope"
        , "pin"
    ]

    wipe_parameters = [
        "wifiMacs"
        , "id"
        , "serial"
        , "pin"
    ]

    check_in_parameters = [
        "wifiMacs"
        , "ids"
        , "serials"
        , "scope"
    ]

    move_parameters = [
        "wifiMacs"
        , "ids"
        , "serials"
        , "scope"
        , "newNetwork"
    ]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def devices(self, query=None):
        """ Returns the Networks SM Devices API Resource. """
        if query is not None:
            query = clean(query, self.devices_parameters)
            query = "?" + urllib.parse.urlencode(query)
        else:
            query = ""
        return self.get("/devices" + query)

    def modify_devices_tags(self, data):
        """ Add, delete, or update the tags of a set of devices. """
        data = clean(data, self.tags_parameters)
        return self.put("/devices/tags", data)

    def modify_device_fields(self, data):
        """ Modify the fields of a device. """
        data = clean(data, self.fields_parameters)
        return self.put("/device/fields", data)

    def lock_devices(self, data):
        """ Lock a set of devices. """
        data = clean(data, self.lock_parameters)
        return self.put("/devices/lock", data)

    def wipe_device(self, data):
        """ Wipe a device. """
        data = clean(data, self.wipe_parameters)
        return self.put("/device/wipe", data)

    def check_in(self, data):
        """ Force check-in a set of devices. """
        data = clean(data, self.check_in_parameters)
        return self.put("/devices/checkin", data)

    def move_devices(self, data):
        """ Move a set of devices to a new network. """
        data = clean(data, self.move_parameters)
        return self.put("/devices/move", data)
