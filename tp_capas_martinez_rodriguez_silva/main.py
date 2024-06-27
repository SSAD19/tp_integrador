from negocio.gestionar_obras import * 
from models.modelo_orm import *
from dao import *
from peewee import *
  
def main():  
  #Primer bloque creamos nuestra base de datos, conexión 
  GestionarObra.conectar_db()
  
  #Creo las tablas necesarias para mi DB desde mis modelos
  #TODO: REVISAR ORDEN DE CREACION DE TABLAS 
  GestionarObra.mapear_orm(Empresa, AreaResponsable)
  GestionarObra.verTablas()
  '''
 
  data =  GestionarObra.cargar_datos()
  GestionarObra.imprimir_data(data)
  '''
  
  #ejemplo de como crear empresa que no se utilizará acá 
  '''try: 
    empresa_dao = EmpresaDao()
    #empresa_dao.crearModelo(razon_social="Mi caminito S.A.", cuit=30123456779, activa=True)
    lista_empresas = empresa_dao.traerTodos()
    for i in lista_empresas: print(i.razon_social, i.cuit)
      
  except Exception as e:
    print("error:", e)'''
 
  GestionarObra.cerrarConex()
  input("presione enter para culminar")
  

  
if __name__ == '__main__':
  try:
    main() 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   
