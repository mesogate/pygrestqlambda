"""
Transform values suitable for sending via JSON
"""

from uuid import UUID
from datetime import datetime


def to_string(value: object) -> str:
    """
    Calculates the string version of an object to return in a JSON response
    """

    # Handle UUIDs
    if isinstance(value, UUID):
        value = str(value)

    # Handle timestamps
    if isinstance(value, datetime):
        value = value.isoformat()

    return value
