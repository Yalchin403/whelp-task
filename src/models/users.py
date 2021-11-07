from config.db import conn
from peewee import *
import datetime
from .index import BaseMOdel, create_tables


class User(BaseMOdel):
    id = PrimaryKeyField()
    age = IntegerField(null=False)
    name = CharField(null=False,  max_length=255)
    surname = CharField(null=False,  max_length=255)
    username = CharField(null=False,  max_length=255)
    email = CharField(null=False,  max_length=255)
    gender = CharField(null=False,  max_length=255)
    password = CharField(null=False,  max_length=255)
    is_admin = BooleanField(default=False)
    is_verified = BooleanField(default=False)


    class Meta:
        db_table = 'users'


create_tables(User)