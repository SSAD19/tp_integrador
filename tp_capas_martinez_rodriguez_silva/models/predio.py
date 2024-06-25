from peewee import *
from base_model import *

class Predio(BaseModel):
    id_predio = AutoField()
    comuna = CharField(unique = True)
    barrio = CharField(unique = True)
    
    class Meta:
        db_table = 'predios'

