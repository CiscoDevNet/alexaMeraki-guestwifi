"""
Meraki API
"""
from .meraki_api_resource import MerakiAPIResource
from .devices import Devices
from .organizations import Organizations
from .networks import Networks


class MerakiAPI(MerakiAPIResource):
    """
    You must instantiate a new object from this class, setting you profile 
    authentication token to access the API.::

        from meraki_api import MerakiAPI

        # Meraki Dashboard API profile authentication token.
        KEY = "MY_AUTHENTICATION_KEY"
        # API root.
        meraki = MerakiAPI(KEY)

    The networks, organizations, and devices endpoints all work in a similar
    manner. They all inherit from ::class:`~meraki_api.meraki_api_resource` ,
    so they have all the command REST actions: `index`, `create`, `show`,
    `update`, and `delete`. Some of them have other special functions to
    execute more specific actions. They also reference other endpoint
    creators.::

        # All organizations.
        organizations = meraki.organizations()
        # List.
        organizations.index()
        # Create new organization.
        organizations.create({"name": "New organization"})

        # To access an individual organization we must pass its ID.
        ORGANIZATION_ID = "MY_ORGANIZATION_ID"
        organization = meraki.organizations(ORGANIZATION_ID)
        # Organization details.
        organization.show()
        # Update organization.
        organization.update({"name": "Updated organization name"})
        # Delete organization.
        organization.delete()

    We would use the same action to interact with the `networks` or `devices`
    endpoints

    .. note::

      Each `index`, `create`, `show`, `update`, and `delete` function, returns a
      `requests` response object. If you just want the body we should run
      `response.json()` to get it.
    """

    def __init__(self, key):
        if key is None:
            raise ValueError("The 'key' value must be defined.")
        MerakiAPIResource.__init__(self, key)

    def organizations(self, organization_id=None):
        """ Returns the API Organizations Resource. """
        return Organizations(self.key, None, organization_id)

    def networks(self, network_id=None):
        """ Returns the API Networks Resource. """
        return Networks(self.key, None, network_id)

    def devices(self, serial=None):
        """ Returns the API Devices Resource. """
        return Devices(self.key, None, serial)
