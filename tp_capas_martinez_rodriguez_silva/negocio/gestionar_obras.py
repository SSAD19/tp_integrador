import abc
import os
import pandas as pd
from utils.db_obras import *
from models.modelo_orm import *

class GestionarObra(abc.ABC):
    
    db = db_sqlite
    
    #Funciona
    #Lógica de negocio asociada a la base de datos 
    #funcion para conectar la base de datos, en caso de cambiar la misma se realizará en utils. 
    @classmethod
    def conectar_db(cls) -> bool:
        try:
            cls.db.connect()
            print("Se conecto")
            return True
        except Exception as e: 
            print("Error!! ", e)
            return False
    
    #funciona 
    #Función para mapear las estructura de la base de datos
    @classmethod
    def mapear_orm(cls, *tablas:BaseModel) -> None: 
        try:
            cls.db.create_tables(tablas)
            print("Tabla creada")
        except Exception as e:
            print("Error al crear la tabla. ", e)
            
         #TODO: EXCEPCIONES PERSONALIZADAS
   
   #funciona
   #Función para cerrar la conexión cuando no sea necesario  realizar acciones con esta
    @classmethod
    def cerrarConex(cls) -> None:
        try: 
             if not cls.db.is_closed:
                 cls.db.close()
                 print('cerro conexion')
        except Exception as e:
            print("Error al cerrar la conexión. ", e) 
    
    #funciona  
    @classmethod        
    def verTablas(cls) -> None:
        try:
            print(cls.db.get_tables())
        except Exception as e:
            print("Error al ver las tablas. ", e)
    
    
    
    #Logica de negocio relacionada a la manipulacion de grandes datos mediante pandas y numpy     
    
    #funciona
    @classmethod
    def extraer_datos(cls, dataframe = None) -> object:  
        try:
            if dataframe is None:
                dataframe = ("tp_capas_martinez_rodriguez_silva\\dataset\\observatorio-de-obras-urbanas.csv")
            
            data = pd.read_csv(dataframe, sep=";",  encoding='ISO-8859-1',  quotechar='"', skip_blank_lines=True)
            return data
        
        except FileNotFoundError as e:
            print("Error al conectar con el dataset.", e)
            return None
        
        except Exception as e: 
            print("Error al importar dataset. ", e)
            return None
    #TODO: EXCEPCIONES PERSONALIZADAS
    
    @classmethod
    def eliminar_columnas(cls, data, columnas) -> object:
        try:
           return data.drop(columns=columnas)
       
        except Exception as e: 
            print('Error', e)  
            return None  
            
    #trabajando en esta funcion
    #TODO: HAY ERROR  'NoneType' object is not subscriptable
    @classmethod
    def limpiar_datos (cls, data, nombreColumna:str):
        if data is False: return None
        
        try:
            data[nombreColumna] = data[nombreColumna].apply(lambda x: x.lower())
            return  data.dropna(subset=[nombreColumna])
        except Exception as e: 
            print("Error, no se pudo ingresar limpiar los registros. ", e)
            return None
    

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
        try: 
        #Imprimir nombres para confirmar datos de columnas
            print(data.columns)
            #Imprimir cantidad total de datos por columna
            #print(data.count())
        except Exception as e:
            print('Erro: ', e)
        
         
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
        '''
        query segun orm peewew para obtener la siguiente informacion :
        a. Listado de todas las áreas responsables.
        b. Listado de todos los tipos de obra.
        c. Cantidad de obras que se encuentran en cada etapa.
        d. Cantidad de obras y monto total de inversión por tipo de obra.
        e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
        f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1.
        g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.

        h. Porcentaje total de obras finalizadas.
        i. Cantidad total de mano de obra empleada.
        j. Monto total de inversión.
        
        '''
        pass 