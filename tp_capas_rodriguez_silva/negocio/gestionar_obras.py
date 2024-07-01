import abc
from itertools import count
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
                
    #Funciona
    @classmethod
    def nueva_obra(cls) -> Obra: 
        try:
           
            #solicito los campos necesarios para generar nuevo proyecto
            expediente = input('indique el expediente de la licitación a crear: ')
            anio= date.today().year
            descripcion= input('Descripción de la licitacion: ')
            
            areas_Todas = AreaResponsable.select()
            for a in areas_Todas:
                print(a.nombre_area)
                
            area_responsable = input('Indique  # el area responsable: ') 
            area =  AreaResponsable.get_or_none(AreaResponsable.nombre_area==area_responsable)
            
            
            licitacion = Licitacion.create(
                                        expediente=expediente, 
                                        licitacion_anio=anio,
                                        area_responsable=area,
                                        descripcion=descripcion
                                        )
            
            
            
            etapa= EtapaObra.get_or_none(EtapaObra.nombre == "nuevo proyecto")
            entorno= input('Indique entorno de la obra: ')
            nombre = input('Indique nombre de la obra: ')
            
            tipo_Todas = TipoObra.select(TipoObra.nombre)
            for a in tipo_Todas:
                print(a.nombre)
                
            tipo = input('Indique tipo de obra: ')
            tipo_obra= TipoObra.get_or_none(TipoObra.nombre == tipo)
          
            
            predio_Todas = Predio.select(Predio.barrio)
            for a in predio_Todas:
                print(a.barrio)
                
            predio= input('Indique el barrio donde se ejecutará la obra: ')
            predio = Predio.get_or_none(Predio.barrio==predio)
            
            comuna=int(input('Indique el número de la comuna donde se ejecutará la obra: '))
            direccion =  input('Indique la dirección donde se ejecutará la obra: ')
            plazo_meses=int(input('indique el numero de meses de contrato estimado: '))
         
            
            nueva_obra_data = {
                    'entorno': entorno,
                    'nombre': nombre,
                    'tipo_obra': tipo_obra,
                    'etapa_obra': etapa,
                    'licitacion': licitacion,
                    'predio': predio,
                    'comuna': comuna,
                    'direccion': direccion,
                    'plazo_meses': plazo_meses,
                    'porcentaje_avance': 0
                 }
            
            obra_nueva = Obra.nuevo_proyecto(nueva_obra_data)
            return obra_nueva
        
        except Exception as e:
            print("Error: ", e)
   
   
   #TESTEO
    @classmethod 
    def nueva_obra_hardcodeada(cls) -> Obra: 
        try:
            etapa = EtapaObra.get_or_none(EtapaObra.nombre == "nuevo proyecto")
           
            area =  AreaResponsable.get_or_none(AreaResponsable.nombre_area=='Ministerio de Salud')
            licitacion = Licitacion.create(
                    expediente='Ex896482-78', 
                    licitacion_anio=date.today().year,
                    area_responsable=area,
                    descripcion='Reparación ruberia'
                    )
            tipo_obra = TipoObra.get(TipoObra.nombre=='Arquitectura')
            predio_buscar= Predio.get(Predio.barrio=='Saavedra')
            obra_data = {
                    'entorno': 'Tubería gas',
                    'nombre': 'Saavedra_vias126',
                    'tipo_obra': tipo_obra ,
                    'etapa_obra': etapa,
                    'licitacion': licitacion,
                    'predio': predio_buscar,
                    'comuna': 12,
                    'direccion': 'Calle plaza',
                    'plazo_meses': 2,
                    'porcentaje_avance': 0
                 }
            
            obra_nueva = Obra()
            obra_nueva = Obra.nuevo_proyecto(obra_data)
            return obra_nueva
        
        except Exception as e:
            print("Error en nueva_obra_hardcodeada: ", e)
       
      
    
    #TODO: desarrollar
    @classmethod
    def obtener_indicadores(cls) -> None: 
        #Funciona
        try:
        # a. Listado de todas las áreas responsables.
            listado_areas= AreaResponsable.select()
            print('Áreas responsable:')
            for i in listado_areas:
                print(f'- {i.id} : {i.nombre_area}')
        except Exception as e:
            print("Error: ", e)
        
        
        #Funciona   
        try:    
            # b. Listado de todos los tipos de obra.
            listado_tipo_obras=TipoObra.select()
            print('Tipos de obras: ')
            for i in listado_tipo_obras:
                print(f'-{i.id}: {i.nombre}')
        except Exception as e:
            print("Error: ", e)
        
        #Funciona
        print('Cantidad de obras por etapa:')
        # c. Cantidad de obras que se encuentran en cada etapa.
        try:  
            obras_por_etapa = (Obra.select(EtapaObra.nombre, fn.COUNT(Obra.id).alias('cantidad'))
                                .join(EtapaObra, on=(Obra.etapa_obra == EtapaObra.id))
                                .group_by(EtapaObra.nombre))
            
            for i in obras_por_etapa:
                print(f'- {i.etapa_obra.nombre}: {i.cantidad}')
        except Exception as e:
            print(f'Error al obtener la cantidad de obras por etapa: {e}')
         
        #Funciona    
        print('Cantidad de obras y monto total de inversión por tipo de obra:')
        try:   
            # d. Cantidad de obras y monto total de inversión por tipo de obra.
            obras_por_tipo = (Obra.select(TipoObra.nombre,
                    fn.COUNT(Obra.id).alias('cantidad_obras'),
                    fn.SUM(Contratacion.monto).alias('monto_total_inversion'))
                .join(TipoObra, on=(Obra.tipo_obra == TipoObra.id))
                .join(Contratacion, on=(Obra.contratacion == Contratacion.id))
                .group_by(TipoObra.nombre))

            for obra in obras_por_tipo:
                print(f'- {obra.tipo_obra.nombre}: {obra.cantidad_obras} obras - Monto total: ${obra.monto_total_inversion:.2f}')
        except Exception as e:
            print("Error: ", e)
            
            
        #Funciona   
        #  e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
        print('Listado de barrios pertenecientes a las comunas 1,2 y 3')
        try:
            barrios_comunas = Predio.select(Predio.barrio).distinct().join(Obra, on=Predio.id == Obra.predio_id).where(
                    Obra.comuna.in_([1, 2, 3]))
            print('Listado de barrios pertenecientes a las comunas 1, 2 y 3:')
            for barrio in  barrios_comunas:
                print(f'- {barrio.barrio}')
                
        except Exception as e:
            print("Error: ", e)
       
        #funciona
        # f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1.
        print("Cantidad de obras finalizadas y monto total de inversión en comuna 1:")
        try:
            obras_finalizadas = (Obra
                .select(fn.COUNT(Obra.id).alias('total_obras'),
                        fn.SUM(Contratacion.monto).alias('monto'))
                .join(Contratacion, on=(Obra.contratacion == Contratacion.id))
                .join(EtapaObra, on=(Obra.etapa_obra == EtapaObra.id))
                .where((Obra.comuna == 1) & (EtapaObra.nombre == 'Finalizada'))
                .group_by(Obra.comuna)
                .get())
            
            print(f'- {obras_finalizadas.total_obras} obras - Monto total: ${obras_finalizadas.monto:.2f}')
        except Exception as e:
            print("Error: ", e)
        
        
        
        # g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
        print("Cantidad de obras finalizadas en un plazo menor o igual a 24 meses:")
        try:
            obras_meses = (
                Obra.select(fn.COUNT(Obra.id))
                .join(EtapaObra)  # Une la tabla EtapaObra
                .where(
                    (EtapaObra.nombre == 'Finalizada') & (Obra.plazo_meses <= 24)
                )
                .scalar()
            )

            if obras_meses is not None:  # Manejo de posibles valores nulos
                print(f"Cantidad de obras: {obras_meses}")
            else:
                print("No se encontraron obras finalizadas en el plazo especificado.")

        except Exception as e:
            print(f"Error al consultar la base de datos: {e}") 


        #Funciona
        #  h. Porcentaje total de obras finalizadas.
        print("Porcentaje total de obras finalizadas:")
        try:
            total_obras = Obra.select().count()
            obras_finalizadas = Obra.select().where(Obra.etapa_obra_id == 1).count()

            if total_obras == 0:
                print("No hay obras registradas.")
            else:
                porcentaje_finalizadas = (obras_finalizadas / total_obras) * 100
                print(f"{porcentaje_finalizadas:.2f}%")

        except Exception as e:
            print(f"Error al consultar la base de datos: {e}")
      
      
        #funciona
        # i. Cantidad total de mano de obra empleada.
        print("Cantidad total de mano de obra empleada:")
        try:
            mano_obra_total = (
                Obra.select(fn.SUM(Contratacion.mano_de_obra))  # Cambio aquí
                .join(Contratacion)                           # Asegura el JOIN a Contratacion
                .scalar() 
            )

            if mano_obra_total is not None:
                print(f"{mano_obra_total}")
            else:
                print("No se encontró mano de obra empleada.")

        except Exception as e:
           print(f"Error al consultar la base de datos: {e}")
        
        #funciona
        #  j. Monto total de inversión.
        print("Monto total de inversión:")
        try:
            monto_inversion_total = (
                Obra.select(fn.SUM(Contratacion.monto))  # Corrección aquí
                .join(Contratacion)                     # Asegura el JOIN a Contratacion
                .scalar()
            )

            if monto_inversion_total is not None:
                print(f"{monto_inversion_total}")
            else:
                print("No se encontró información sobre montos de inversión.")

        except Exception as e:
            print(f"Error al consultar la base de datos: {e}")