"""
Transform provided object into requested MIME type
"""

from enum import Enum

class MimeType(str, Enum):
    """
    Supported subset of common MIME types
    """
    PDF = "application/pdf"
    CSV = "text/csv"
    JSON = "application/json"


def get_mime_type(accept: str | None) -> MimeType | None:
    """
    Get MIME type based on Accept header string
    """

    # Check if a mimetype is set, use JSON by default
    if not accept:
        return MimeType.JSON

    # Attempt to initialise the enum with the provided value
    try:
        MimeType(accept)
        return MimeType
    except ValueError:
        return None


class MimeTypeTransformer:
    """
    Class to transform raw data into the requested MIME type
    """

    def __init__(self, data: object, mime_type: MimeType):
        self.data = data
        self.mime_type = mime_type


    def run(self) -> str | bytes | None:
        """
        Transform data into requested MIME type
        """

        if self.mime_type == MimeType.JSON:
            return self.get_json()

        if self.mime_type == MimeType.CSV:
            return self.get_csv()

        if self.mime_type == MimeType.PDF:
            return self.get_pdf()

        return None


    def get_pdf(self):
        """
        Get PDF representation of data
        """

        return ''

    def get_json(self):
        """
        Get JSON representation of data
        """

        return '{"example": "data"}'

    def get_csv(self):
        """
        Get CSV representation of data
        """

        return ''
