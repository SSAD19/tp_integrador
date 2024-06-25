from peewee import *
from base_model import *

class AreaResponsable(BaseModel):
    id_area = AutoField(primary_key= True)
    nombre_area = CharField(unique = True, max_length=100)
    
    class Meta:
        db_table= 'area_respondable'    
        