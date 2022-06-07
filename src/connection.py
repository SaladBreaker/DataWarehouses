import logging

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from src.models import Asset, Data, Source

KEYSPACE = "test"

logger = logging.getLogger(__name__)


def setup_connection():
    connection.setup(["127.0.0.1"], "test", protocol_version=4)
    connection.execute(
        f"CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} "
        "WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};"
    )


def sync_tables():
    setup_connection()
    sync_table(Asset)
    sync_table(Data)
    sync_table(Source)
    logger.info(f"Synced tables to Cassandra at 127.0.0.1 using keyspace: {KEYSPACE}")

