"""
Meraki SAML Roles API Resource
"""

from .meraki_api_resource import MerakiAPIResource


class SAMLRoles(MerakiAPIResource):
    """ Meraki API Organization SAML Roles resource. """

    resource = "samlRoles"

    parameters = ["role", "orgAccess", "networks", "tags"]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
