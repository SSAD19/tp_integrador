import abc
import peewee as pw
import pandas as pd
from utils.db_obras import *
from models.modelo_orm import *
import asyncio

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
        except pw.OperationalError as e:
            print("Error al conectar a la base de datos: ", e)
            return False
        except pw.InternalError as e:
            print("Error interno al conectar a la base de datos: ", e)
            return False
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
    def extraer_datos(cls, dataframe=None) -> object:  
        try:
            if dataframe is None:
                dataframe = ("tp_capas_rodriguez_silva\\dataset\\observatorio-de-obras-urbanas.csv")
            
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
    #TODO: HAY ERROR , pareceria no estar eliminando espacios en blanco (?)
    @classmethod
    def limpiar_datos (cls, data, nombreColumna=None):
        if data is False: return None
        
        if nombreColumna == None:
            return data.dropna()
        try:
            return data.dropna(subset=[nombreColumna])
        except Exception as e: 
            print("Error, no se pudo ingresar a limpiar los registros. ", e)
            return 
    

     #función para eliminar datos repetidos 
    
    #funciona
    @classmethod
    def datos_unique(cls, data, nombreColumna=None):
        if data is False: return
        try:
            if nombreColumna==None: 
                return data.drop_duplicates()
            else:
                data_clean = cls.limpiar_datos(data, nombreColumna)
                return list(data_clean[nombreColumna].unique())
        
        except Exception as e:
            print("Error, no se pudo unificar el listado. ", e)
            return
   
    #funciona
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
        
    #TODO: unificar aca haciendo primerlo la limpieza de datos   
    @classmethod
    async def cargar_datos(cls, model:Model, atributos) -> None:
        try:
        # model.bulk_create(*atributos)
         #TODO: cambiar a model.create(*atributos)
            model.create(**atributos)
            
        except DatabaseError as e:
            print("Error en database: ", e)
        except Exception as e: 
            print(e)
            
    #TODO:desarrollar 
    @classmethod
    def nueva_obra(cls, *args) -> None: 
        pass 
    
    #TODO: desarrollar
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