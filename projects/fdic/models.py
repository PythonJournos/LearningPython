# Import our library.
from peewee import *

# Connect to the DB.
db = SqliteDatabase('fdic.sqlite')


# Set up a bank.
class Bank(Model):
    """
    This defines a bank and all of the fields a bank has.
    """
    bank = CharField()
    city = CharField()
    state = CharField()
    cert_num = PrimaryKeyField()
    acq_inst = CharField()
    closed = DateField()
    updated = DateField()
    url = CharField()

    # What is this thing?
    class Meta:
        """
        It's a class INSIDE a class.
        Don't let that bother you.
        We need to attach this model to a database.
        Also, we need to point to Schnaars's table.
        """
        database = db
        db_table = 'failed_banks'
