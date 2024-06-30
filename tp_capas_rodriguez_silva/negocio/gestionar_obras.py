import abc
import peewee as pw
import pandas as pd
from utils.db_obras import *
from models.modelo_orm import *
from datetime import date 

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
    async def cargar_datos_subclase(cls, model:Model, atributos) -> None:
        try:
           
            model.create(**atributos)
            
        except DatabaseError as e:
            print("Error en database: ", e)
        except Exception as e: 
            print(e)
  
    @classmethod
    async def cargar_datos(cls, data:pd.DataFrame) -> None:
        try: 
           for _, row in data.iterrows():
               Contratacion.create(nro_contratacion=row['nro_contratacion'],
                                   tipo_contratacion=TipoContratacion.select().where(TipoContratacion.nombre==row['tipo']),
                                   empresa=row['licitacion_oferta_empresa'],
                                   mano_de_obra=row['mano_obra'],
                                   monto=row['monto_contrato']
                                   )
               Licitacion.create(
                   expediente=row['expediente-numero'],
                   licitacion_anio=row['licitacion_anio'],
                   descripcion=row['descripcion'],
                   area_responsable=AreaResponsable.select().where(AreaResponsable.nombre_area==row['area_responsable']),
                   pliego=row['pliego_descarga']
                   )             
               Obra.create(
                   entorno=row['entorno'],
                   nombre=row['nombre'],
                   tipo_obra=TipoObra.select().where(TipoObra.nombre==row['tipo']),
                   etapa_obra=EtapaObra.select().where(EtapaObra.nombre==row['etapa']),
                   licitacion=Licitacion.select().where(Licitacion.expediente==row['expediente-numero']),
                   contratacion=Contratacion.select().where(Contratacion.nro_contratacion==row['nro_contratacion']),
                   predio=Predio.select().where(Predio.barrio==row['barrio']),
                   comuna=row['comuna'],
                   direccion=row['direccion'],
                   lat=row['lat'],
                   long=row['lng'],
                   fecha_inicio=row['fecha_inicio'],
                   fecha_estimada_fin=row['fecha_fin_inicial'],
                   plazo_meses=row['plazo_meses']                  
                   )
        except OperationalError as e:
            print("No se han podido cargar los datos", e)
                  
        except Exception as e:
            print("Error: ", e)
                
    #TODO:desarrollar 
    @classmethod
    def nueva_obra(cls) -> None: 
        pass 
    
    #TODO: desarrollar
    @classmethod
    def obtener_indicadores(cls) -> None: 
        
        
        #Funciona
        # try:
        # # a. Listado de todas las áreas responsables.
        #     listado_areas= AreaResponsable.select(AreaResponsable.nombre_area)
        #     print('Áreas responsable:')
        #     for i in listado_areas:
        #         print(f'-{i.nombre_area}')
        # except Exception as e:
        #     print("Error: ", e)
        
        
        #Funciona   
        # try:    
        #     # b. Listado de todos los tipos de obra.
        #     listado_tipo_obras=TipoObra.select(TipoObra.nombre)
        #     print('Tipos de obras: ')
        #     for i in listado_tipo_obras:
        #         print(f'-{i.nombre}')
        # except Exception as e:
        #     print("Error: ", e)
        
        print('Cantidad de obras por etapa:')    
        try:    
            # c. Cantidad de obras que se encuentran en cada etapa.
            obras_por_etapa = (Obra.select(Obra.etapa_obra.nombre, fn.COUNT(Obra.id).alias('cantidad')).group_by(Obra.etapa_obra.id))
           
           
            for i in obras_por_etapa:
                print(f'- {i.etapa_obra.nombre}: {(i.cantidad)}')
        except Exception as e:
            print("Error: ", e)
            
        
        # print('Cantidad de obras y monto total de inversión por tipo de obra:')     
        # try:   
        #     # d. Cantidad de obras y monto total de inversión por tipo de obra.
        #     obras_por_tipo = (Obra.select(Obra.tipo_obra.nombre,
        #             fn.COUNT(Obra.id).alias('cantidad_obras'),
        #             fn.SUM(Contratacion.monto).alias('monto_total_inversion'))
        #         .join(Obra.contratacion)
        #         .group_by(Obra.tipo_obra.nombre))

        #     for obra in obras_por_tipo:
        #         print(f'- {obra.tipo_obra.nombre}: {obra.cantidad_obras} obras - Monto total: ${obra.monto_total_inversion:.2f}')
        
        # except Exception as e:
        #     print("Error: ", e)
        
        # #Funciona
        # # try:   
        # # # e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
        # #     barrios_comunas = Predio.select(Predio.barrio).distinct().join(Obra, on=Predio.id == Obra.predio_id).where(
        # #             Obra.comuna.in_([1, 2, 3]))
        # #     print('Listado de barrios pertenecientes a las comunas 1, 2 y 3:')
        # #     for barrio in  barrios_comunas:
        # #         print(f'- {barrio.barrio}')
                
        # # except Exception as e:
        # #     print("Error: ", e)
       
        # # f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1.
       
       
        # print("Cantidad de obras finalizadas y monto total de inversion en comuna 1: ")
        # try:           
        #     obras_finalizadas = Obra.select(fn.COUNT(Obra.nombre), fn.SUM(Obra.contratacion.monto)).where(Obra.comuna ==1)
            
        #     print(f'- {obras_finalizadas.nombre}: {obras_finalizadas.contratacion.monto:.2f}')
       
        # except Exception as e:
        #     print("Error: ", e)
        
       
        # # g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
        # print("Cantidad de obras finalizadas en un plazo menor o igual a 24 meses:")
        # try:
           
        #     obra_meses = Obra.select(fn.COUNT(Obra.id)).where(Obra.etapa_obra.nombre == 'Finalizada') & (Obra.plazo_meses >= 24)
        #     print(f" {obra_meses}")
        # except Exception as e:
        #     print("Error: ", e)

        # # h. Porcentaje total de obras finalizadas.
        # print("Porcentaje total de obras finalizadas:")
        # try: 
        #     total_obras = Obra.select().count()
        #     obras_finalizadas = Obra.select().where(Obra.etapa_obra.id == 1).count()

        #     porcentaje_finalizadas = (obras_finalizadas / total_obras) * 100

        #     print(f" {porcentaje_finalizadas:.2f}%")
        
        # except Exception as e:
        #     print("Error: ", e)
        
        # # i. Cantidad total de mano de obra empleada.
        # print("Cantidad total de mano de obra empleada:")
        # try:
        #     mano_obra_total = Obra.select(fn.SUM(Obra.contratacion.mano_de_obra))
        #     print(f" {mano_obra_total}")
            
        # except Exception as e:
        #     print("Error: ", e)
        
        
        # # j. Monto total de inversión.
        # print("Monto total de inversión:")
        # try:           
        #     monto_inversion_total = Obra.select(fn.SUM(Obra.contratacion.monto))
        #     print(f" {monto_inversion_total}")
        # except Exception as e:
        #     print("Error: ", e)
   