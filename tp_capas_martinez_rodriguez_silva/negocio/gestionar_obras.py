import abc
import os
import pandas as pd
from utils.db_obras import *
from models.modelo_orm import *

class GestionarObra(abc.ABC):
    
    db = db_sqlite
    #Lógica de negocio asociada a la base de datos 
    @classmethod
    def conectar_db(cls) -> bool:
        try:
            cls.db.connect()
            print("Se conecto")
            return True
        except Exception as e: 
            print("Error!! ", e)
            return False
    
    @classmethod
    def mapear_orm(cls, *tablas:BaseModel) -> None: 
        try:
            cls.db.create_tables(tablas)
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)
            
         #TODO: EXCEPCIONES PERSONALIZADAS
    @classmethod
    def cerrarConex(cls) -> None:
        try: 
             if not cls.db.is_closed:
                 cls.db.close()
                 print('cerro conexion')
        except Exception as e:
            print("Error al cerrar la conexión. ", e) 
      
    @classmethod        
    def verTablas(cls) -> None:
        try:
            print(cls.db.get_tables())
        except Exception as e:
            print("Error al ver las tablas. ", e)
    
    
    
    #Logica de negocio relacionada a la manipulacion de grandes datos mediante pandas y numpy     
    @classmethod
    def extraer_datos(cls, dataframe = None):  
        try:
            if dataframe is None:
                dataframe = ("tp_capas_martinez_rodriguez_silva\\dataset\\observatorio-de-obras-urbanas.csv")
            
            data = pd.read_csv(dataframe, sep=",", skip_blank_lines=True)
            return data
        
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            return False
        
        except Exception as e: 
            print("Error al importar dataset. ", e)
            return False
    
    #TODO: EXCEPCIONES PERSONALIZADAS
    @classmethod
    def limpiar_datos (cls,data, nombreColumna:str):
        if data is False: return
        
        try:
            return data.dropna(subset=[f'{nombreColumna}'], axis =0, inplace= True)
        
        except Exception as e: 
            print("Erros, no se pudo ingresar limpiar los registros. ", e)
            return 
    
    
     #función para eliminar datos repetidos 
    @classmethod
    def datos_unique(cls,data, nombreColumna:str) -> list:
        if data is False: return
        try:
            return list(data[f'{nombreColumna}'].unique())
        
        except Exception as e:
            print("Erros, no se pudo unificar el listado. ", e)
            return
    
    @classmethod    
    def imprimir_data(cls, data) -> None:
        #en caso de haber algún error en la data retorna sin hacer nada
        if data is False: return
        
        #Imprimir nombres para confirmar datos de columnas
        print(data.columns)
        #Imprimir cantidad total de datos (?)
        print(data.count())
        
        #TODO: Chequear como se ven esos datos por consola 
        
         
    #TODO:
    @classmethod
    def cargar_datos(cls, *args) -> None:
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
    
    #TODO:
    @classmethod
    def nueva_obra(cls, *args) -> None: 
        pass 
    
    #TODO:
    @classmethod
    def obtener_indicadores(cls, *args) -> None: 
        pass 