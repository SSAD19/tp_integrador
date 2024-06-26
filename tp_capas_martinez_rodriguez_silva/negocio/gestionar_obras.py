import abc
from negocio.importar_datos import ManejoDatos

class GestionarObra(abc.ABCMeta):
    #TODO: Revisar en detalle los argumentos pasados para verificarq ue estén correctos y los retornos
    
    @abc.abstractmethod
    def extraer_datos(self, *args)-> object: 
        #Debe incluir las sentencias necesarias para manipular el dataset usando pandas 
        pass
        
    
    @abc.abstractmethod
    def conectar_db(self, *args) -> bool:
        #conexcion a base de dato
        pass
    
    @abc.abstractmethod
    def mapear_orm(self, **args) -> object: 
        #crear la estructura de la base de datos mediante el uso de modelos de peewee
        pass
    
    @abc.abstractmethod
    def limpiar_datos(drlf,*args) -> bool:
        pass
    
    @abc.abstractmethod
    def cargar_datos(self, *args) -> None:
        pass
    
    @abc.abstractmethod
    def nueva_obra(self, *args) -> None: 
        pass 
    
    @abc.abstractmethod
    def obtener_indicadores(self, *args) -> None: 
        pass 