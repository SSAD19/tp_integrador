from peewee import *
from utils import db_obras


class TipoContratacion(Model):
    id = AutoField(primary_key=True)
    nombre_tipo = CharField(unique = True)
    
    class Meta:
        db = db_obras.db 
        db_table = 'tipo_contratacion'


