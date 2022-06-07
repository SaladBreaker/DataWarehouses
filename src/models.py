import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Asset(Model):
    id = columns.Integer(primary_key=True)
    name = columns.Text(required=True)
    description = columns.Text(required=False)
    system_date = columns.DateTime(default=datetime.datetime.now())
    additional_attributes = columns.Map(columns.Text, columns.Text)


class Data(Model):
    asset_id = columns.Integer(partition_key=True)
    source_id = columns.Integer(partition_key=True)
    business_date = columns.DateTime()
    system_date = columns.DateTime(default=datetime.datetime.now())
    values_double = columns.Map(columns.Text, columns.Float)
    values_text = columns.Map(columns.Text, columns.Text)
    values_integer = columns.Map(columns.Text, columns.Text)


class Source(Model):
    id = columns.Integer(primary_key=True)
    name = columns.Text(required=True)
    description = columns.Text(required=False)
    publisher = columns.Text(required=False)
    system_date = columns.DateTime(default=datetime.datetime.now())
    attributes = columns.Map(columns.Text, columns.Text)

