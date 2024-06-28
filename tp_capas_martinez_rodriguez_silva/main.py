from negocio.gestionar_obras import * 
from models.modelo_orm import *
from dao.dao import *
from peewee import *
  
def main():  
  #Primer bloque creamos nuestra base de datos, conexión 
  GestionarObra.conectar_db()
  
  #Creo las tablas necesarias para mi DB desde mis modelos
  #TODO: REVISAR ORDEN DE CREACION DE TABLAS 
  GestionarObra.mapear_orm(AreaResponsable, TipoObra, TipoContratacion, Predio, Empresa, Contratacion, Licitacion, EtapaObra, Obra)
  GestionarObra.verTablas()
  

  data = GestionarObra.extraer_datos()
  columnas=['plazo_meses', 'imagen_1', 'imagen_2', 'imagen_3', 'imagen_4', 
            'beneficiarios', 'compromiso', 'destacada', 'ba_elige', 'link_interno', 'estudio_ambiental_descarga',
            'financiamiento', 'Unnamed: 36']
  
  data = GestionarObra.eliminar_columnas(data, columnas)

  GestionarObra.imprimir_data(data)
  
  
  '''
  primero  generar las tablas que no están relacionadas a otras y ver si son uniques 
  limpiar area responsable

  '''
  #Por probar!!!!! 
  area_data = GestionarObra.limpiar_datos( data, 'area_responsable')
  listaLimpia = GestionarObra.datos_unique(area_data, "area_responsable")
  
  for i in listaLimpia:
    
    area = AreaResponsableDao()
    area.crearModelo(i)
    
 
  GestionarObra.cerrarConex()
  input("presione enter para culminar")
  

  
if __name__ == '__main__':
  try:
    main() 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   
