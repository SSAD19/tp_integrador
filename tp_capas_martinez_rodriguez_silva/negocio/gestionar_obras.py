import abc
from negocio.importar_datos import ManejoDatos
from utils.db_obras import db_sqlite
import pandas as pd
import numpy as np


class GestionarObra(abc.ABCMeta):
    #TODO: Revisar en detalle los argumentos pasados para verificarq ue estén correctos y los retornos
    
    
    #Lógica de negocio asociada a la base de datos 
    db = db_sqlite
    
    def conectar_db(self, *args) -> bool:
        try:
            self.db.connect()
            print("Se conecto")
            return True
        except Exception as e: 
            print("Error!! ", e)
            return False
    
    def mapear_orm(self, *tabla) -> None: 
        try:
            self.db.create_tables([*tabla])
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)
            
         #TODO: EXCEPCIONES PERSONALIZADAS
    
    def cerrarConex(self):
        try: 
             if not self.db.is_closed:
                 self.db.close()
                 print('cerro conexion')
        except Exception as e:
            print("Error al cerrar la conexión. ", e) 
    
    
    
    #Logica de negocio relacionada a la manipulacion de grandes datos mediante pandas y numpy     
    def extraer_datos(self, dataframe = ".\dataset\observatorio-de-obras-urbanas.csv")-> pd.DataFrame:  
        try:
            data = pd.read_csv(dataframe, sep=",")
            return data
        
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            return False
        
        except Exception as e: 
            print("Error al importar dataset. ", e)
            return False
    
    @abc.abstractmethod
    def limpiar_datos(drlf, data, nombreColumna:str):
        if data is False: return
        
        try:
            return data.dropna(subset=[f'{nombreColumna}'], axis =0, inplace= True)
        
        except Exception as e: 
            print("Erros, no se pudo ingresar limpiar los registros. ", e)
            return 
    
    
     #función para eliminar datos repetidos 
    def datos_unique(data, nombreColumna:str) -> list:
        if data is False: return
        try:
            return list(data[f'{nombreColumna}'].unique())
        
        except Exception as e:
            print("Erros, no se pudo unificar el listado. ", e)
            return
        
    def imprimir_data(data) -> None:
        #en caso de haber algún error en la data retorna sin hacer nada
        if data is False: return
        
        #Imprimir nombres para confirmar datos de columnas
        print(data.columns)
        #Imprimir cantidad total de datos (?)
        print(data.count())
        
        #TODO: Chequear como se ven esos datos por consola 
        
         
    
    
    @abc.abstractmethod
    def cargar_datos(self, *args) -> None:
        #TODO: sentencias necesarias para pasar persistir data del dataframe en DB
        '''
          #cargar Empresas 
  datos_obras_urbanas = eliminar_vacios(datos_obras_urbanas, 'licitacion_oferta_empresa')
  Empresas = datos_unique(datos_obras_urbanas, 'licitacion_oferta_empresa')
  
  for i in Empresas: 

    try: 
      if datos_obras_urbanas['licitacion_oferta_empresa'].str.contains(i):
        cuit = datos_obras_urbanas['cuit_contratista']
      else:
        cuit = None
        
      EmpresaD.create(licitacion_oferta_empresa = i,
                     cuit_contratista =cuit)
      
    except DatabaseError as e: 
      print(f"Error al crear empresa {e}")
      
    except Exception as e:
      print(f"Error al crear empresa {e}")
        
        
        '''
        #hacerlo en el mosulo CargaDatos
        
        
        pass
    
    @abc.abstractmethod
    def nueva_obra(self, *args) -> None: 
        pass 
    
    @abc.abstractmethod
    def obtener_indicadores(self, *args) -> None: 
        pass 