from peewee import (
    Model,
    IntegerField,
    CharField,
    SqliteDatabase,
    FloatField,
    BlobField
)

db = SqliteDatabase('../data/dev_database.db')


class Users(Model):
    id = IntegerField()
    name = CharField()
    email = CharField()
    wallet_uuid = CharField()
    deleted = IntegerField()

    class Meta:
        database = db
        # table_name = users => can add table name into meta


class Transactions(Model):
    id = IntegerField()
    timestamp = IntegerField()
    cost = IntegerField()
    sellers_wallet_uuid = CharField()
    customer_wallet_uuid = CharField()
    product_uuid = IntegerField()
    delivery_option = CharField()
    longitude = FloatField()
    latitude = FloatField()

    class Meta:
        database = db


class Products(Model):
    id = IntegerField()
    cost = IntegerField()
    sellers_uuid = CharField()
    description = CharField()
    name = CharField()
    deleted = IntegerField()
    image = BlobField()

    class Meta:
        database = db
