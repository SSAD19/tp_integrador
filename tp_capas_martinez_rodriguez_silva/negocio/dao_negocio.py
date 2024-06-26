from negocio.gestionar_obras import GestionarObra
from utils import db_obras


class BaseDatos(GestionarObra):
    
    db = db_obras.db_sqlite
    
    def conectar_db(self) -> bool:
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
    
    
    
    def mapear_orm(self, *tabla) -> object:
        try:
            self.db.create_tables([*tabla])
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)