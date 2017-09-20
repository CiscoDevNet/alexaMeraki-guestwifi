Meraki Dashboard API
~~~~~~~~~~~~~~~~~~~~

Meraki API is a wrapper around requests library to interact with the Meraki
Dashboard API. It simplifies interacting with the API by keeping track of the
users token, handling query and body parameters, and has the ability to execute
the request lazily.

First, we can bootstrap the module by indicating our API Key.

  >>> import MerakiAPI
  >>> KEY = <Your user Meraki API KEY>
  >>> meraki = MerakiAPI(KEY)

After this we don't have to worry again about it. To get the a list
of all the organizations we would call the `organizations().index()` function.

  >>> response = meraki.organizations().index()

This will return a `requests` response object. If we want to get the json data
from the response, we just call `.json()` over it.

  >>> json = response.json()

If we want to set up the request to call it in the future we can use the `lazy`
function before calling on `index`.

  >>> lazy_request = meraki.organizations().lazy().index()

This will return a `LazyRequests` object that holds the request action until we
need to run it. It is also useful to check the URL that was created, without
actually generating a request to the API.

  >>> lazy_request.get_url()
  "https://dashboard.meraki.com/api/v0/organizations"

When we feel like it we can use the `call` function inside out `LazyRequests`
object to send the request to the Server. This will also return a `requests`
response object.

  >>> lazy_request.call()

All the endpoints specified as of July 1 2017 are defined.
You can see the official documentation at:

  https://dashboard.meraki.com/api_docs

:copyright: (c) 2017 by Guzmán Monné.
:license: MIT, see LICENSE for more details.
