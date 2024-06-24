from peewee import *
from utils import db_obras

class Predio(Model):
    id_predio = AutoField()
    comuna = CharField(unique = True)
    barrio = CharField(unique = True)
    
    class Meta:
        db = db_obras.db
        db_table = 'predios'

