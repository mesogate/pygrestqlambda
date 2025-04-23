"""
Pytest configuration file, sets up fixtures to be re-used and set up pre-test
configuration.
Uses [docker](https://docker-py.readthedocs.io/en/stable/index.html) python
client to manage container.
"""

from pytest import fixture
from tests.integration.utils.constants import POSTGRES_NAME
from tests.integration.utils.db_postgres import get_postgres_connection
from tests.integration.utils.docker import remove_container

@fixture(scope="session")
def postgres():
    """
    Return a psycopg database connection
    """

    return get_postgres_connection()


def pytest_sessionfinish():
    """
    Runs after all tests have completed
    Tear down containers.
    """

    remove_container(POSTGRES_NAME)
