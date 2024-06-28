from negocio.gestionar_obras import * 
from models.modelo_orm import *
from dao.dao import *
from peewee import *
  

  
def limpiar_y_cargar_daraframe(dataframe,nombreColumna:str, unico:bool, model:Model):
    
    try:
      filtro1 = GestionarObra.limpiar_datos( dataframe, nombreColumna)
      print(filtro1[nombreColumna])
      if unico:
        listaLimpia = GestionarObra.datos_unique(filtro1, nombreColumna)
        print(listaLimpia)    
        lista_fin = [AreaResponsable(nombre_area=area) for area in listaLimpia] 
      
      else: 
        lista_fin = [AreaResponsable(nombre_area=area) for area in filtro1[nombreColumna]]
      
      GestionarObra.cargar_datos(AreaResponsable, lista_fin) 
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
  GestionarObra.imprimir_data(data)
  
  limpiar_y_cargar_daraframe(data, 'area_responsable',True, AreaResponsable)

  
  
  #Esto funciona! 
  '''
  area_data = GestionarObra.limpiar_datos( data, 'area_responsable')
  print(area_data['area_responsable'])
  listaLimpia = GestionarObra.datos_unique(area_data, 'area_responsable')
  print(listaLimpia)
  
  
  areas = [AreaResponsable(nombre_area=area) for area in listaLimpia] 
  GestionarObra.cargar_datos(AreaResponsable, areas) 
  '''
 
  GestionarObra.cerrarConex()
  input("presione enter para culminar")
  

  
if __name__ == '__main__':
  try:
    main() 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   
