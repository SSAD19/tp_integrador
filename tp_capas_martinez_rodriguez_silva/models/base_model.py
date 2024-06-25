from peewee import *
from utils import db_obras


class BaseModel(Model):
    
    class Meta:
        database = db_obras.db_sqlite