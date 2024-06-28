from peewee import *
from models.modelo_orm import *

class BaseDao:
    def __init__(self, model:Model):
        self.model = model
   
     #TODO: Métodos CRUD con models
     
    def crear_modelo(self, **kwargs):
        try:
            self.model.create(**kwargs)
        except Exception as e: 
            print(e)
        
    def borrar_modelo(self, id:int):
        try: 
            query = self.model.delete().where(self.model.id_pk == id)
            query.execute()
        except Exception as e: 
            print(e)
        
    def traer_todos (self):
        try: 
            return list(self.model.select())
        except Exception as e:
            print(e) 
            
    #TODO:  Probar , en caso de no funcionar se modificara por cada entidad en DAO
    def traer_uno (self,id):
        return self.model.get().where(self.model.id_pk ==id)
    
    def actualizarModelo (self, id:int, *kwargs):
        query = self.model.update(*kwargs).where(self.model.id_pk == id)
        query.execute()
    


class AreaResponsableDao(BaseDao):
    def __init__(self):
        super().__init__(AreaResponsable)
        
    def traer_por_nombre (self, nombre):
        return self.model.select().where(self.model.nombre_area == nombre)
        
        
class ContrataciondesDao(BaseDao):
    def __init__(self):
        super().__init__(Contratacion)
        
    '''
        query = Stat.update(counter=Stat.counter + 1).where(Stat.url == request.url)
        query.execute()
    
    '''

class EmpresaDao(BaseDao):
    def __init__(self):
        super().__init__(Empresa)
        
class EtapaObraDao(BaseDao):
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
     