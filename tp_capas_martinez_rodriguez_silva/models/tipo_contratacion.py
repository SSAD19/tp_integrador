from peewee import *
from models.base_model import *


class TipoContratacion(BaseModel):
    id_tipo_contratacion= AutoField(primary_key=True)
    nombre_tipo = CharField(unique = True)
    
    class Meta:
        db_table = 'tipo_contratacion'


