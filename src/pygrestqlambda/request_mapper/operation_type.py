"""
Operation type enumerations
"""

from enum import Enum

class OperationType(Enum):
    """
    Enum representing the operations that can be performed on resources
    """

    # Create - maps to HTTP: PUT and POST
    CREATE_SINGLE = 'CREATE_SINGLE'
    CREATE_MULTIPLE = 'CREATE_MULTIPLE'
    # Read - maps to HTTP: GET
    READ_SINGLE = 'READ_SINGLE'
    READ_MULTIPLE = 'READ_MULTIPLE'
    # Update - maps to HTTP: PATCH
    UPDATE_SINGLE = 'UPDATE_SINGLE'
    UPDATE_MULTIPLE = 'UPDATE_MULTIPLE'
    # Delete - maps to HTTP: DELETE
    DELETE_SINGLE = 'DELETE_SINGLE'
    DELETE_MULTIPLE = 'DELETE_MULTIPLE'
