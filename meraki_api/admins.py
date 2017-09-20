"""
Meraki Admins API Resource
"""

from .meraki_api_resource import MerakiAPIResource

class Admins(MerakiAPIResource):
    """ Meraki API Organization Admins resource. """

    resource = "admins"

    parameters = ["email", "name", "orgAccess", "tags", "networks"]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
