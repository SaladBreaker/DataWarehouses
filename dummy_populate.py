import json
import logging

from src.connection import setup_connection
from src.models import Asset, Source, Data

import pandas as pd

logger = logging.getLogger(__name__)


def dummy_populate_database():
    setup_connection()
    logger.info("Adding dummy entries to DB...")

    data = pd.read_csv('./sources/asset.csv')

    index = 1
    for entry in data.to_dict('records'):
        entry["additional_attributes"] = json.loads(entry["additional_attributes"])
        entry["id"] = index
        Asset.create(**entry)
        index += 1

    data = pd.read_csv('./sources/source.csv')

    index = 1
    for entry in data.to_dict('records'):
        entry["attributes"] = json.loads(entry["attributes"])
        entry["id"] = index
        Source.create(**entry)
        index += 1

    data = pd.read_csv('./sources/data.csv')

    for entry in data.to_dict('records'):
        entry["values_double"] = json.loads(entry["values_double"])
        entry["values_text"] = json.loads(entry["values_text"])

        Data.create(**entry)

    logger.info("Finished dummy entries to DB!")
