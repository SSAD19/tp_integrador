from peewee import *
from models.base_model import BaseModel
from models import tipo_contratacion as tp, empresas as em 


class Contratacion(BaseModel): 
    id_contratacion = AutoField(primary_key=True)
    nro_contratacion = CharField(unique=True)
    tipo_contratacion = ForeignKeyField(tp.TipoContratacion) 
    empresa = ForeignKeyField(em.Empresa)    
    mano_de_obra = IntegerField()
    
    class Meta:
        db_table = 'contrataciones'


