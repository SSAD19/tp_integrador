#Clases y atribuos definidos para consumo de la orm 
#nombre base de datos en sqlite: 'obras_urbanas.db' -> ubicada en la misma carpeta

from peewee import *

db_sqlite = SqliteDatabase('obras_urbanas.db')


def conectar_base(self) -> bool:
      try:
         db_sqlite.connect()
         return True
      #excepcion personalizada (?)
      except Exception as e:
         print(f"Error al conectar a la base de datos: {e}")
         return False
      
class BaseModel():
   class Meta:
      database = db_sqlite
      
 
class Empresa(Model):
   licitacion_oferta_empresa = CharField()
   cuit_contratista = CharField(unique = True, primary_key= True)
   
   class Meta: 
      db_table = 'empresas'


#TODO: FINALIZADAS LAS CLASES, CREAR TABLAS EN SQLITE
db_sqlite.create_tables([Empresa])
'''
 clases definidas por el momento: 
    Empresa
    Lugar
    Contratacion
    Licitacion
    Obra
    
    subtablas definidas: 
    tipo_contratacion
    tipo_obra
    etapa_obra 
 
'''