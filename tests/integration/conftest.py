"""
Pytest configuration file, sets up fixtures to be re-used and set up pre-test
configuration.
Uses [docker](https://docker-py.readthedocs.io/en/stable/index.html) python
client to manage postgres container.
"""

from pytest import fixture
from tests.integration.utils import (
    wait_for_postgres_container,
    remove_postgres_container,
    get_postgres_connection,
)


def pytest_configure():
    """
    Runs before any tests, starts up postgres database to be used by tests.
    Starts container on a random port and wait until a successful login is made.
    """

    wait_for_postgres_container()


def pytest_unconfigure():
    """
    Runs after all tests, removes postgres container set up for this test suite
    """

    remove_postgres_container()


@fixture(scope="session")
def db():
    """
    Return a psycopg database connection
    """

    return get_postgres_connection()
