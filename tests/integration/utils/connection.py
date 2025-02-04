"""
Utility functions for connecting to database
"""

import logging
from time import sleep
import psycopg
from psycopg import Error
from psycopg.connection import Connection
from psycopg.rows import dict_row

def get_db_connection() -> Connection:
    """

    """

    max_retries = 20

    config = {
        'host': 'db',
        'port': 5432,
        'user': 'pytest',
        'password': 'pytest',
        'dbname': 'pytest',
        'sslmode': 'require',
    }

    for i in range(1, max_retries + 1):
        logging.info("Attempt %s to connect to database", i)
        try:
            with psycopg.connect(**config) as conn:
                conn.row_factory = dict_row
                result = conn.execute('SELECT 3 + 2 AS test;').fetchone()
                assert result['test'] == 5
                logging.info('Successfully connected to database')
                return conn
        except Error as exc:
            if i < max_retries:
                logging.info(exc)
                logging.info('Database not ready, waiting')
                sleep(3)
            else:
                raise ConnectionError(
                    f'Database not ready after {max_retries} retries'
                ) from exc
