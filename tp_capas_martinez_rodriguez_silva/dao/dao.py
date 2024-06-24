
from models import *


class Dao:
    def __init__(self, model) -> None:
        self.model = model
   
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