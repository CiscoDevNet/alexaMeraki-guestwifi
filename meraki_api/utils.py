"""
meraki_api.utils
~~~~~~~~~~~~~~~~
This module provides utility functions that are used within meraki_api
that are also useful for external consumption.
"""

def clean(data, parameters):
    """
    Cleans a dictionary to only includ valid parameters and non empty values.
    """
    # Only take valid parameters.
    data = {key: data.get(key) for key in parameters}
    # Remove empty parameters.
    data = {key: value for key, value in data.items() if value is not None}
    return data
