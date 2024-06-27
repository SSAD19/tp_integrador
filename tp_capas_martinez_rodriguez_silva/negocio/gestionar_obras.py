import abc
from peewee import *
import pandas as pd
from utils.db_obras import db_sqlite
#from models import empresas as em, area_responsable as ar, contrataciones as con, licitacion as li, predio as pr, etapa_obra as eo, obra as ob, tipo_contratacion as tc, tipo_obra as to




class GestionarObra(abc.ABCMeta):
    
    #Lógica de negocio asociada a la base de datos 
    
    
    def conectar_db(db = db_sqlite) -> bool:
        try:
            db.connect()
            print("Se conecto")
            return True
        except Exception as e: 
            print("Error!! ", e)
            return False
    
    def mapear_orm(db = db_sqlite, *tabla:Model) -> None: 
        try:
            db.create_tables([*tabla])
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)
            
         #TODO: EXCEPCIONES PERSONALIZADAS
    
    def cerrarConex(db = db_sqlite) -> None:
        try: 
             if not db.is_closed:
                 db.close()
                 print('cerro conexion')
        except Exception as e:
            print("Error al cerrar la conexión. ", e) 
            
    def verTablas(db = db_sqlite ) -> None:
        try:
            print(db.get_tables())
        except Exception as e:
            print("Error al ver las tablas. ", e)
    
    
    
    #Logica de negocio relacionada a la manipulacion de grandes datos mediante pandas y numpy     
    def extraer_datos(dataframe = "dataset\observatorio-de-obras-urbanas.csv")-> pd.DataFrame:  
        try:
            data = pd.read_csv(dataframe, sep=",")
            return data
        
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            return False
        
        except Exception as e: 
            print("Error al importar dataset. ", e)
            return False
    
    #TODO: EXCEPCIONES PERSONALIZADAS
    def limpiar_datos (data, nombreColumna:str):
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
        
         
    #TODO:
    def cargar_datos(*args) -> None:
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
    def nueva_obra(*args) -> None: 
        pass 
    
    #TODO:
    def obtener_indicadores(*args) -> None: 
        pass 