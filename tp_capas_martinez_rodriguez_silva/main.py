from negocio.gestionar_obras import * 
from peewee import *
  

  
def carga_df_un_campo(dataframe, nombreColumna:str, unico:bool, model:Model, field_name:str ):
  try:
    filtro1 = GestionarObra.limpiar_datos(dataframe, nombreColumna)
    print(filtro1[nombreColumna])
    
    if unico:
      listaLimpia = GestionarObra.datos_unique(filtro1, nombreColumna)
      print(listaLimpia) 
     
      lista_fin = [model(**{field_name: item}) for item in listaLimpia] 
    
    else: 
      lista_fin = [model(**{field_name: item}) for item in filtro1[nombreColumna]]
    
    GestionarObra.cargar_datos(model, lista_fin) 
    
  except Exception as e:
    
    print(e)



def main():  
  #Primer bloque creamos nuestra base de datos, conexión 
  GestionarObra.conectar_db()
  
  #Creo las tablas necesarias para mi DB desde mis modelos
  GestionarObra.mapear_orm(AreaResponsable, TipoObra, TipoContratacion, Predio, Empresa, Contratacion, Licitacion, EtapaObra, Obra)
  GestionarObra.verTablas()
  
  #Extraigo los datos del dataSet .- trae un path por defecto, pero puede ingresarse para reutilizacion en otros casos
  data = GestionarObra.extraer_datos()
  
  #Iniciamos la limpieza de los datos migrados eliminando las columnas que no vamos a utilizar
  columnas=['plazo_meses', 'imagen_1', 'imagen_2', 'imagen_3', 'imagen_4', 
            'beneficiarios', 'compromiso', 'destacada', 'ba_elige', 'link_interno', 'estudio_ambiental_descarga',
            'financiamiento', 'Unnamed: 36']  
  data = GestionarObra.eliminar_columnas(data, columnas)

  #Revisamos que la data haya quedado correcta según las necesidades
  #GestionarObra.imprimir_data(data)
  '''
    'id', 'entorno', 'nombre', 'etapa', 'tipo', 'area_responsable',
       'descripcion', 'monto_contrato', 'comuna', 'barrio', 'direccion', 'lat',
       'lng', 'fecha_inicio', 'fecha_fin_inicial', 'porcentaje_avance',
       'licitacion_oferta_empresa', 'licitacion_anio', 'contratacion_tipo',
       'nro_contratacion', 'cuit_contratista', 'mano_obra', 'pliego_descarga',
       'expediente-numero'],
      dtype='object')
  '''
  
    
  #Carga de subtablas con datos de un campo
  carga_df_un_campo(data, 'area_responsable',True, AreaResponsable, 'area_responsable')
  #eliminar campos mal escritos 
  carga_df_un_campo(data, 'tipo', True,  TipoObra, 'nombre')
  #eliminar campos mal escritos
  carga_df_un_campo(data,'etapa', True, EtapaObra, 'nombre')
  #eliminar campos mal escritos
  
  
  """  try:
    filtro1 = GestionarObra.limpiar_datos(data, 'area_responsable')
    listaLimpia = GestionarObra.datos_unique(filtro1, 'area_responsable')
    print(listaLimpia) 
    lista_fin = [AreaResponsable(nombre_area=item) for item in listaLimpia]  
    GestionarObra.cargar_datos(AreaResponsable, lista_fin) 
    
  except Exception as e: 
    print(e)
  
  try:
    filtro1 = GestionarObra.limpiar_datos(data, 'tipo')
    listaLimpia = GestionarObra.datos_unique(filtro1, 'tipo')
    print(listaLimpia) 
    lista_fin = [TipoObra(nombre=item) for item in listaLimpia]  
    GestionarObra.cargar_datos(TipoObra, lista_fin) 
    
  except Exception as e: 
    print(e)
  
  try:
    filtro1 = GestionarObra.limpiar_datos(data, 'tipo')
    listaLimpia = GestionarObra.datos_unique(filtro1, 'tipo')
    print(listaLimpia) 
    lista_fin = [TipoObra(nombre=item) for item in listaLimpia]  
    GestionarObra.cargar_datos(TipoObra, lista_fin) 
    
  except Exception as e: 
    print(e)
  
  """
  
  GestionarObra.cerrarConex()
  input("presione enter para culminar")
  

  
if __name__ == '__main__':
  try:
    main() 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   
