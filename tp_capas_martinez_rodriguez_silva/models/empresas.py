from peewee import *
from models.base_model import *

class Empresa (BaseModel):
    id_empresa = AutoField(primary_key=True)
    razon_social = CharField(unique=True)
    cuit = IntegerField(unique=True)
    activa = BooleanField(default=True) 
    
    class Meta:
        db_table = 'empresas'