from config.db import conn
from peewee import *
import datetime


class BaseMOdel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = conn


def create_tables(table_name):
    with conn:
        conn.create_tables([table_name])
