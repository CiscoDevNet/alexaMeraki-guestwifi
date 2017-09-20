"""
Meraki API Resource
"""
import json
from .lazy_requests import LazyRequests

class MerakiAPIResource:
    """ Simplifies the creation of Meraki API resources. """

    url = "https://dashboard.meraki.com/api/v0"
    resource = ""

    parameters = []
    cached = None
    is_lazy = False

    def __init__(self, key, prefix=None, resource_id=None):
        self.resource_id = resource_id
        self.key = key
        self.prefix = prefix

    def __headers(self):
        """ Returns the needed headers. """
        return {
            "Content-Type": "application/json",
            "X-Cisco-Meraki-API-Key": self.key
        }

    def check_for_resource_id(self):
        """ Raises an exception if the resource_id is not defined. """
        if self.resource_id is None:
            raise ValueError("Can't access without a resource_id")

    def endpoint(self):
        """ Builds the endpoint. """
        endpoint = ""
        if self.prefix is not None:
            endpoint += str(self.prefix)
        if self.resource is not None:
            endpoint += "/" + str(self.resource)
        if self.resource_id is not None:
            endpoint += "/" + str(self.resource_id)
        return endpoint

    def lazy(self):
        """ Turns the class lazy. """
        self.is_lazy = True
        return self

    def set_resource_id(self, resource_id=None):
        """ Sets the resource_id value. """
        if resource_id is not None:
            self.resource_id = str(resource_id)
        else:
            self.resource_id = None
        return self

    def use(self, resource_id):
        """
        Alias to set_resource_id for better chaining.
        The only difference with this function is that the
        `resource_id` parameter is now required.
        """
        return self.set_resource_id(resource_id)

    def dynamic(self):
        """ Makes the class dynamic (not lazy). """
        self.is_lazy = False
        return self

    def __build_url(self):
        """ Builds the url. """
        url = self.url + str(self.endpoint())
        return url

    def set_resource_id(self, resource_id):
        """ Sets the resource_id value. """
        self.resource_id = resource_id
        return self

    def call(self):
        """ Calls the cached function. """
        return self.cached.call()

    def get_url(self):
        """ Gets the cached url. """
        return self.cached.url or "No url cached yet."

    def index(self):
        """ Get all the resources. """
        return self.get()

    def show(self):
        """ Gets a resource. """
        return self.get()

    def request(self, method, suffix=None, data=None):
        """ Dynamically create and call LazyRequest methods. """
        url = self.__build_url() + (str(suffix) if suffix is not None else "")
        headers = self.__headers()
        if data is not None:
            data = json.dumps(data)
        func = getattr(LazyRequests(url, headers, data), method, None)
        if func is None:
            raise ValueError("The method wanted does not exists in the class.")
        self.cached = func()
        return self if self.is_lazy is True else self.cached.call()

    def get(self, suffix=None):
        """
        Returns a class that can call a ger request to a built URL lazily.
        """
        return self.request("get", suffix)

    def post(self, suffix=None, data=None):
        """
        Returns a class that can call a post request to a built URL lazily.
        """
        return self.request("post", suffix, data)

    def put(self, suffix=None, data=None):
        """
        Returns a class that can call a put request to a built URL lazily.
        """
        return self.request("put", suffix, data)

    def create(self, data):
        """ Create a new resource. """
        return self.request("post", None, data)

    def update(self, data):
        """ Updates a resource. """
        return self.request("put", None, data)

    def delete(self):
        """ Deletes a resouce. """
        return self.request("delete", None)
