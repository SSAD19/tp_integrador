import abc

class GestionarObra(abc):
    #TODO: Revisar en detalle los argumentos pasados para verificarq ue estén correctos y los retornos
    
    
    @abc.abstractmethod
    def extraer_datos(self, *args) -> None: 
        pass
    
    @abc.abstractmethod
    def conectar_db(self) -> bool:
        pass
    
    @abc.abstractmethod
    def mapear_orm(self) -> object: 
        pass