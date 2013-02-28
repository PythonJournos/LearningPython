from peewee import *

db = SqliteDatabase('fdic.sqlite')


class Bank(Model):
    bank = CharField()
    city = CharField()
    state = CharField()
    cert_num = PrimaryKeyField()
    acq_inst = CharField()
    closed = DateField()
    updated = DateField()
    url = CharField()

    class Meta:
        database = db
        db_table = 'failed_banks'
