from peewee import *
from models.area_responsable import *
from models.base_model import *

class Licitacion(BaseModel):
    
    nro_expediente = CharField(unique = True, primary_key = True)
    licitacion_anio = DateField()
    descripcion = TextField()
    area_responsable = ForeignKeyField(AreaResponsable)
    #Este campo es la URL donde pueden descargar los pliegos que estarán en una base de dato externa -nube/servidor
    pliegos= CharField()
    
    
    class Meta:
        db_table= 'licitaciones'    
        
        
    