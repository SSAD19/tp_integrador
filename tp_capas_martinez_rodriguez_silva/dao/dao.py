from peewee import *
from models import *

class BaseDao:
    def __init__(self, model):
        self.model = model
   
     #TODO: Métodos CRUD con models
     
    def crearModelo(self, **kwargs):
        try:
            self.model.create(**kwargs)
        except Exception as e: 
            print(e)
        
    def borrarModelo(self, id):
        try: 
            query = self.model.delete().where(self.model.id == id)
            query.execute()
        except Exception as e: 
            print(e)
        
    def traerTodos (self):
        try: 
            return list(self.model.select())
        except Exception as e:
            print(e) 
   
   
   
    #TODO:  Probar , en caso de no funcionar se modificara por cada entidad en DAO
    def traerUno (self, **kwargs):
        return self.model.get(**kwargs)
    
    def actualizarModelo (self, **kwargs):
        query = self.model.update().where(kwargs)
        query.execute()
    
    