"""
Meraki Config Templates API Resource
"""

from .meraki_api_resource import MerakiAPIResource

class ConfigTemplates(MerakiAPIResource):
    """ Meraki Config Templates API Resource. """

    resource = "configTemplates"

    def __init__(self, key, prefix=None, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)
