from peewee import *
from models.base_model import *


class TipoContratacion(BaseModel):
    id = AutoField(primary_key=True)
    nombre_tipo = CharField(unique = True)
    
    class Meta:
        db_table = 'tipo_contratacion'


