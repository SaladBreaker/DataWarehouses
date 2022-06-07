import logging
import os

from dummy_populate import dummy_populate_database
from logging_config import configure_logging
from src.connection import  sync_tables

if __name__ == '__main__':
    if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
        os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

    configure_logging(level=logging.INFO)

    sync_tables()
    dummy_populate_database()

