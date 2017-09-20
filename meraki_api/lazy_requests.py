"""
Lazy Requests.
---

Class that can cache a request methods for later invocation.
"""

import requests


class LazyRequests():
    """
    Allow to call requests lazily. When called you should provide all the
    necessary parameters to call make the request. By default the *header* and
    the *url* are mandatory. The *data* parameter is optional, and should only
    be provided if we want to call a `put` or `post` request.
    """

    cached = None

    def __init__(self, url, headers, data=None):
        self.url = url
        self.headers = headers
        self.data = data

    def cache(self, method):
        """
        Caches a function that calls a requests method with the saved params.
        """
        def func():
            """ Function wrapper to lazily invoke requests.get. """
            data = self.data if method == 'post' or 'put' else None
            request_method = getattr(requests, method, None)
            return request_method(self.url, headers=self.headers, data=data)
        self.cached = func
        return self

    def call(self):
        """ Invokes the cached function or throws an error. """
        if self.cached is None:
            raise ValueError("No cached function found.")
        return self.cached()

    def get(self):
        """
        Caches a function that calls requests.get with current parameters.
        """
        return self.cache('get')

    def post(self):
        """
        Caches a function that calls requests.post with current parameters.
        """
        return self.cache('post')

    def put(self):
        """
        Caches a function that calls requests.put with current parameters.
        """
        return self.cache('put')

    def delete(self):
        """
        Caches a function that calls requests.delete with current parameters.
        """
        return self.cache('delete')
