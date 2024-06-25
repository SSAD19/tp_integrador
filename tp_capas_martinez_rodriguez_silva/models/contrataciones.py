from peewee import *
from tipo_contratacion import TipoContratacion
from base_model import *


class Contratacion(BaseModel): 
    nro_contratacion = CharField(unique=True, primary_key=True)
    tipo_contratacion = ForeignKeyField(TipoContratacion)     
    #TODO: completar campos -> Empresa, mano_de_obra 
    
    class Meta:
        db_table = 'contrataciones'


