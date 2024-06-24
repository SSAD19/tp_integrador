from peewee import *
from utils import db_obras
from area_responsable import *

class Licitacion(Model):
    
    nro_expediente = CharField(unique = True, primary_key = True)
    licitacion_anio = DateField.year()
    descripcion = TextField()
    area_responsable = ForeignKeyField(AreaResponsable)
    #Este campo es la URL donde pueden descargar los pliegos que estarán en una base de dato externa -nube/servidor
    pliegos= CharField()
    
    
    class Meta:
        db = db_obras.db
        db_table= 'licitaciones'    
        
        
    