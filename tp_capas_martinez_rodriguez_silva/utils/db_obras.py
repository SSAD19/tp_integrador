from peewee import SqliteDatabase
from models import *


# db = db_sqlite = SqliteDatabase('obras_urbanas.db')

class BaseDatos:
    
    db = SqliteDatabase('obras_urbanas.db')
    
    def abrirConex(self) -> bool:
        try:
            self.db.connect()
            print("Se conecto")
            return True
        except Exception as e: 
            print("Error!! ", e)
            return False
        #excepciones personalizadas: 
            
    def cerrarConex(self):
        try: 
             if not self.db.is_closed:
                 self.db.close()
                 print('cerro conexion')
        except Exception as e:
            print("Error al cerrar la conexión. ", e)
            
    def crearTabla(self): 
        try:
            self.db.create_tables([Empresa, ])
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)