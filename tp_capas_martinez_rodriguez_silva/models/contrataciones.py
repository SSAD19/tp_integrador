from peewee import *
from tipo_contratacion import TipoContratacion
from utils import db_obras

class Contratacion(Model): 
    nro_contratacion = CharField(unique=True, primary_key=True)
    tipo_contratacion = ForeignKeyField(TipoContratacion)     
    #TODO: completar campos -> Empresa, mano_de_obra 
    
    class Meta:
        db = db_obras.db
        db_table = 'contrataciones'


