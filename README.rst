Alexa Meraki Lamba Function Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This repo contains many packages that are required in order to create the upload package(.ZIP) for Amazon Lambda.

There is the Meraki API (Meraki API is a wrapper around requests library to interact with the Meraki
Dashboard API. It simplifies interacting with the API by keeping track of the
users token, handling query and body parameters, and has the ability to execute
the request lazily.)
This is from Guzmán Monné
:copyright: (c) 2017 by Guzmán Monné.
:license: MIT, see LICENSE for more details.

Other packages include requests which have been downloaded in the directory.

Finally there is the lambda_function.py which is the actual function. This file has multiple functions defined which will be called when a particular intent is called.
