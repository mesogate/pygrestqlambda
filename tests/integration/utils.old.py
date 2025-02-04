"""
Integration testing utilities
"""

import logging
from time import sleep
from uuid import uuid4
import docker
from docker.models.containers import Container
from docker.errors import NotFound
import psycopg
from psycopg import Error
from psycopg.connection import Connection
from psycopg.rows import dict_row

POSTGRES_IMAGE = 'postgres:17'
POSTGRES_NAME = f'pytest-postgres-{str(uuid4())}'
POSTGRES_DB = 'pytest'
POSTGRES_USER = 'pytest'
POSTGRES_PASSWORD = 'pytest'


def create_postgres_container() -> Container:
    """
    Create local PostrgeSQL docker container
    """

    logging.info('Starting postgres container %s', POSTGRES_NAME)
    client = docker.from_env()
    postgres_container = client.containers.run(
        image=POSTGRES_IMAGE,
        name=POSTGRES_NAME,
        detach=True,
        ports={'5432/tcp': None},
        environment={
            'POSTGRES_DB': POSTGRES_DB,
            'POSTGRES_USER': POSTGRES_USER,
            'POSTGRES_PASSWORD': POSTGRES_PASSWORD,
        },
        command="""
            -c ssl=on
            -c ssl_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
            -c ssl_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
        """
    )

    logging.info(
        'Started container %s with id: %s',
        postgres_container.name,
        postgres_container.id,
    )

    return postgres_container


def get_postgres_container() -> Container:
    """
    Return the running postgres Docker container
    """

    client = docker.from_env()
    container = client.containers.get(container_id=POSTGRES_NAME)

    return container


def get_postgres_connection() -> Connection:
    """
    Return a connection to the running postgres container
    """

    try:
        container = get_postgres_container()
    except NotFound:
        container = create_postgres_container()

    port = container.ports['5432/tcp'][0]['HostPort']

    config = {
        'host': '127.0.0.1',
        'port': port,
        'user': POSTGRES_USER,
        'password': POSTGRES_PASSWORD,
        'dbname': POSTGRES_DB,
        'sslmode': 'require',
    }

    return psycopg.connect(**config)


def wait_for_postgres_container():
    """
    Start a container and wait until authentication is available
    """

    max_retries = 20

    for i in range(1, max_retries + 1):
        logging.info('Database connection attempt %s', i)

        try:
            with get_postgres_connection() as conn:
                conn.row_factory = dict_row
                result = conn.execute('SELECT 3 + 2 AS test;').fetchone()
                assert result['test'] == 5
                logging.info('Successfully connected to database')
                return
        except Error as exc:
            if i < max_retries:
                logging.info(exc)
                logging.info('Database not ready, waiting')
                logging.info(exc)
                sleep(3)
            else:
                raise ConnectionError(
                    f'Database not ready after {max_retries} retries'
                ) from exc


def remove_postgres_container():
    """
    Remove Postgres container
    """

    logging.info('Attempting to stop postgres container %s', POSTGRES_NAME)
    container = get_postgres_container()
    logging.info('Container state: %s', container.status)

    if container.status == 'running':
        logging.info('Stopping container id: %s', container.id)
        container.stop()

    logging.info('Removing container id: %s', container.id)
    container.remove()
