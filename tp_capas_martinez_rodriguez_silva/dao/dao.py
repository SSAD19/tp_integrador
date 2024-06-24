import utils.db_obras 
from models import *


class Dao:
    
    db_sqlite = utils.db_obras
    
    def __init__(self, model) -> None:
        self.model = model
    
    def conectar_base(self) -> bool:
      try:
         self.db_sqlite.connect()
         print("Conexion exitosa")
         return True
      #excepcion personalizada (?)
      except Exception as e:
         print(f"Error al conectar a la base de datos: {e}")
         return False
     
     
     #TODO: Métodos CRUD con models
     
    def crearModelo(self, *args):
        return self.model.create(*args)
    
    def borrarModelo(self, id):
        query = self.model.delete().where(self.model.id == id)
        query.execute()
    
    def actualizarModelo (self, id):
        query = self.model.update().where(self.model.id == id)
        query.execute()
    
    def traerTodos (self):
        return list(self.model.select())