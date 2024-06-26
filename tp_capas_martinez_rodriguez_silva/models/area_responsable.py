from peewee import *
from models.base_model import *

class AreaResponsable(BaseModel):
    id_area = AutoField(primary_key= True)
    nombre_area = CharField(unique = True, max_length=100)
    
    class Meta:
        db_table= 'areas_respondables'    
        