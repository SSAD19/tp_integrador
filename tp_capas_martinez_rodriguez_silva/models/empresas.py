from peewee import *
from models.base_model import *

class Empresa (BaseModel):
    razon_social = CharField(unique = True)
    cuit = IntegerField(unique=True, primary_key=True)
    activa = BooleanField(default=True) 
    
    class Meta:
        db_table = 'Empresa'