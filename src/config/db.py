from sqlalchemy import create_engine, MetaData
from peewee import *
from dotenv import load_dotenv
import os


load_dotenv()
db_name = os.getenv("db_name")
user = os.getenv("user")
password = os.getenv("MYSQ_PASSWORD")
host = os.getenv("host")

conn = MySQLDatabase(
    db_name, 
    user=user,
    host=host,
    password=password,
    port=3306
)
meta = MetaData()