from negocio.gestionar_obras import * 
from peewee import *
from pandas import *
  
  # def cargando_dataframe_un_campo(dataframe):
 
  # try:
  #   listado = GestionarObra.datos_unique(dataframe, 'area_responsable')
  #   listado_clean = [AreaResponsable(nombre_area= item) for item in listado]
  #   GestionarObra.cargar_datos(AreaResponsable, listado_clean)
    
  #   listado = GestionarObra.datos_unique(dataframe, 'tipo')
  #   listado_clean = [TipoObra(nombre= item) for item in listado]
  #   GestionarObra.cargar_datos(TipoObra, listado_clean)
    
  #   listado = GestionarObra.datos_unique(dataframe, 
  #                                        'contratacion_tipo')
  #   listado_clean = [TipoContratacion(nombre= item) for item in listado]
  #   GestionarObra.cargar_datos(TipoContratacion, listado_clean)
    
  #   listado = GestionarObra.datos_unique(dataframe, 'etapa')
  #   listado_clean = [EtapaObra(nombre= item) for item in listado]
  #   GestionarObra.cargar_datos(EtapaObra, listado_clean)
    
  #   listado = GestionarObra.datos_unique(dataframe, 'barrio')
  #   listado_clean = [Predio(nombre= item) for item in listado]
  #   GestionarObra.cargar_datos(Predio, listado_clean)
  
  
  # except Exception as e:
  #   print("Error al cargar los datos")

def main_revisando():  
  #Primer bloque creamos nuestra base de datos, conexión 
  GestionarObra.conectar_db()
  
  #Creo las tablas necesarias para mi DB desde mis modelos
  GestionarObra.mapear_orm(AreaResponsable, TipoObra, TipoContratacion, Predio, Empresa, Contratacion, Licitacion, EtapaObra, Obra)
  GestionarObra.verTablas()
  
  #Extraigo los datos del dataSet .- t
  # rae un path por defecto, pero puede ingresarse para reutilizacion en otros casos
  data = GestionarObra.extraer_datos()
  
  #Iniciamos la limpieza de los datos migrados eliminando las columnas que no vamos a utilizar
  columnas=['plazo_meses', 'imagen_1', 'imagen_2', 'imagen_3', 'imagen_4', 
            'beneficiarios', 'compromiso', 'destacada', 'ba_elige', 'link_interno', 'estudio_ambiental_descarga',
            'financiamiento', 'Unnamed: 36', 'comuna']  
  data = GestionarObra.eliminar_columnas(data, columnas)

  #TODO: DESBLOQUEAR
  #Función que me crea cada campo, TODO: Hacer una sola que solo meta varios campos
  cargando_dataframe_un_campo(data)
  
  
  #TODO: IMPORTACION DE EMPRESAS Y  TABLAS MÁS COMPLEJAS
  
  #de varios campos
  #paso columnas a utilizar
  
  data_empresa = data[['licitacion_oferta_empresa', 'cuit_contratista']]
  print(data_empresa.count())
  
  data_empresa = GestionarObra.limpiar_datos(data_empresa)
  print(data_empresa.count())

  razon_social = GestionarObra.datos_unique(data_empresa)
  print(data_empresa)
  print(razon_social)
  
  print(data_empresa.columns)
  
  empresa=[]
  try:
      for index, r in data_empresa.iterrows(): 
              
        empresa[index]=Empresa(razon_social=r['licitacion_oferta_empresa'], cuit=r['cuit_contratista'])
        GestionarObra.cargar_datos(Empresa, empresa[index])       
    
  except Exception as e:
    print("Error al cargar los datos", e)
  
  
  
  #data_empresa_clean = [Empresa(razon_social=item['licitacion_oferta_empresa'], cuit = item['cuit_contratista'])for item in data_empresa]
  #GestionarObra.cargar_datos(Empresa, data_empresa_clean)
  
    #  listado_clean = [AreaResponsable(nombre_area= item) for item in listado]
    #  GestionarObra.cargar_datos(AreaResponsable, listado_clean)

  GestionarObra.cerrarConex()
  input("presione enter para culminar")
  
  
  
  
  #Revisamos que la data haya quedado correcta según las necesidades
  #GestionarObra.imprimir_data(data)
  '''
    'id', 'entorno', 'nombre', 'etapa', 'tipo', 'area_responsable',
       'descripcion', 'monto_contrato', 'barrio', 'direccion', 'lat',
       'lng', 'fecha_inicio', 'fecha_fin_inicial', 'porcentaje_avance',
       'licitacion_oferta_empresa', 'licitacion_anio', 'contratacion_tipo',
       'nro_contratacion', 'cuit_contratista', 'mano_obra', 'pliego_descarga',
       'expediente-numero'],
      dtype='object')
 
   '''
  

  

  
if __name__ == '__main__':
  try:
    main() 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   
