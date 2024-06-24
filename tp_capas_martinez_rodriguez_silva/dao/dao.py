
from models import *


class BaseDao:
    def __init__(self, model) -> None:
        self.model = model
   
     #TODO: Métodos CRUD con models
     
    def crearModelo(self, *args):
        query = self.model.create(*args)
        query.execute()
        
    def borrarModelo(self, id):
        query = self.model.delete().where(self.model.id == id)
        query.execute()
        
    def traerTodos (self):
        return list(self.model.select())
    
    #TODO:  Probar , en caso de no funcionar se modificara por cada entidad en DAO
    def traerUno (self, pk, pk_search):
        return self.model.get(pk=pk_search)
    
    def actualizarModelo (self, pk, pk_search):
        query = self.model.update().where(pk == pk_search)
        query.execute()
    
    