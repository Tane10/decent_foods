from peewee import Model, IntegerField, CharField, SqliteDatabase

db = SqliteDatabase('../data/dev_database.db')


class Users(Model):
    id = IntegerField()
    name = CharField()
    email = CharField()
    wallet_uuid = CharField()
    deleted = IntegerField()

    class Meta:
        database = db
