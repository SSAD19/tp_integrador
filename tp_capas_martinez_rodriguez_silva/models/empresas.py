from peewee import *
from utils import db_obras

class Empresa (Model):
    razon_social = CharField(unique = True)
    cuit = IntegerField(unique=True, primary_key=True)
    activa = BooleanField(default=True) 
    
    class Meta:
        db = db_obras.db
        db_table = 'empresas'