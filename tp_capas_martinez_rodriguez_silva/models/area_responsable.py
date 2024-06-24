from peewee import *
from utils import db_obras

class AreaResponsable(Model):
    id_area = AutoField(primary_key= True)
    nombre_area = CharField(unique = True, max_length=100)
    
    
    class Meta:
        db = db_obras.db
        db_table= 'area_respondable'    
        