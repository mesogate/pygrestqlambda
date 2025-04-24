"""
HTTP Method enumerations
"""

from enum import Enum

class HttpMethod(Enum):
    """
    HTTP methods that may be performed on resources
    """
    # Create
    PUT = 'PUT'
    POST = 'POST'
    # Read
    GET = 'GET'
    # Update
    PATCH = 'PATCH'
    # Delete
    DELETE = 'DELETE'
