from peewee import *
from models.modelo_orm import *

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
            query = self.model.delete().where(self.model.id_pk == id)
            query.execute()
        except Exception as e: 
            print(e)
        
    def traerTodos (self):
        try: 
            return list(self.model.select())
        except Exception as e:
            print(e) 
            
    #TODO:  Probar , en caso de no funcionar se modificara por cada entidad en DAO
    def traerUno (self, *kwargs):
        return self.model.get().where(kwargs)
    
    def actualizarModelo (self, *kwargs):
        query = self.model.update().where(kwargs)
        query.execute()
    


class AreaResponsableDao(BaseDao):
    def __init__(self):
        super().__init__(AreaResponsable)
        
        
class ContrataciondesDao(BaseDao):
    def __init__(self):
        super().__init__(Contratacion)

class EmpresaDao(BaseDao):
    def __init__(self):
        super().__init__(Empresa)
        
class EtapaOnraDao(BaseDao):
    def __init__(self):
        super().__init__(EtapaObra)


class LicitacionDao(BaseDao):
    def __init__(self):
        super().__init__(Licitacion)
        
class AreaResponsableDao(BaseDao):
    def __init__(self):
        super().__init__(Obra)
        

class PredioDao(BaseDao):
    def __init__(self):
        super().__init__(Predio)
        
class TipoContratacionDao(BaseDao):
    def __init__(self):
        super().__init__(TipoContratacion)
        
        
class TipoObraDao(BaseDao):
    def __init__(self):
        super().__init__(TipoObra)
        
        
class ObraDao(BaseDao):
    def __init__(self):
        super().__init__(Obra)