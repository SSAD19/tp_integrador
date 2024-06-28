from negocio.gestionar_obras import * 
from peewee import *
from pandas import *
  
def cargando_dataframe_un_campo(dataframe):
  #TODO:  LIMPIAR PARA NO REPETIR CODIGO
  listado = GestionarObra.datos_unique(dataframe, 'area_responsable')
  listado_clean = [AreaResponsable(nombre_area= item) for item in listado]
  GestionarObra.cargar_datos(AreaResponsable, listado_clean)
  
  listado = GestionarObra.datos_unique(dataframe, 'tipo')
  listado_clean = [TipoObra(nombre= item) for item in listado]
  GestionarObra.cargar_datos(TipoObra, listado_clean)
  
  listado = GestionarObra.datos_unique(dataframe, 'contratacion_tipo')
  listado_clean = [TipoContratacion(nombre= item) for item in listado]
  GestionarObra.cargar_datos(TipoContratacion, listado_clean)
  
  listado = GestionarObra.datos_unique(dataframe, 'etapa')
  listado_clean = [EtapaObra(nombre= item) for item in listado]
  GestionarObra.cargar_datos(EtapaObra, listado_clean)


def main():  
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

  cargando_dataframe_un_campo(data)
  
  
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
   
