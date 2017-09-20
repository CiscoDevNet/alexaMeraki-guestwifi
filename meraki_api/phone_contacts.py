"""
Meraki Phone Contacts API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class PhoneContacts(MerakiAPIResource):
    """ Meraki API Phone Contacts resource. """

    resource = "phoneContacts"

    parameters = ["name"]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
