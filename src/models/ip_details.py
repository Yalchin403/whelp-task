from config.db import conn
from peewee import *
from .index import BaseMOdel, create_tables


class IpDetail(BaseMOdel):


    id = PrimaryKeyField()
    ip = CharField(null=False,  max_length=255)
    details = CharField(null=False,  max_length=255)
    
    class Meta:
        db_table = 'ip_details'


create_tables(IpDetail)