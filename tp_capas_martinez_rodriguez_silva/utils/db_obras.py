from peewee import SqliteDatabase
from models import *
from negocio.gestionar_obras import GestionarObra


db_sqlite = SqliteDatabase('obras_urbanas.db')

class BaseDatos(GestionarObra):
    
    db = db_sqlite
    
    def conectar_db(self) -> bool:
        try:
            self.db.connect()
            print("Se conecto")
            return True
        except Exception as e: 
            print("Error!! ", e)
            return False
        
        #TODO:excepciones personalizadas
            
    def cerrarConex(self):
        try: 
             if not self.db.is_closed:
                 self.db.close()
                 print('cerro conexion')
        except Exception as e:
            print("Error al cerrar la conexión. ", e)
            
        #TODO: EXCEPCIONES PERSONALIZADAS
    
    def mapear_orm(self, *tabla) -> object: 
        try:
            self.db.create_tables([*tabla])
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)
            
         #TODO: EXCEPCIONES PERSONALIZADAS