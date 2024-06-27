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
  GestionarObra.imprimir_data(data)
  

 
  GestionarObra.cerrarConex()
  input("presione enter para culminar")
  

  
if __name__ == '__main__':
  try:
    main() 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   
