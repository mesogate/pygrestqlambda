"""
Supported MIME types enum, a subset of:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
"""

from enum import Enum

class MimeType(str, Enum):
    """
    Supported subset of common MIME types
    """

    PDF = "application/pdf"
    CSV = "text/csv"
    JSON = "application/json"
