import abc

class GestionarObra(abc.ABCMeta):
    #TODO: Revisar en detalle los argumentos pasados para verificarq ue estén correctos y los retornos
    
    
    @abc.abstractmethod
    def extraer_datos(self, *args) -> None: 
        pass
    
    @abc.abstractmethod
    def conectar_db(self, *args) -> bool:
        pass
    
    @abc.abstractmethod
    def mapear_orm(self, **args) -> object: 
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