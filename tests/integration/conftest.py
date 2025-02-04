"""
Pytest configuration file, sets up fixtures to be re-used and set up pre-test
configuration.
Uses [docker](https://docker-py.readthedocs.io/en/stable/index.html) python
client to manage postgres container.
"""

from pytest import fixture
from tests.integration.utils.connection import get_db_connection

@fixture(scope="session")
def db():
    """
    Return a psycopg database connection
    """

    return get_db_connection()
