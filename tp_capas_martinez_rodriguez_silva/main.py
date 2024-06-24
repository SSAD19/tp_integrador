from sqlite3 import OperationalError
from  utils.db_obras import *
from models import *
from peewee import *


  
def main():  
  
  db_sqlite = BaseDatos()
  
  db_sqlite.abrirConex()
  
  db_sqlite.crearTabla('Empresa')
  
  db_sqlite.cerrarConex()
  
  input("presione enter para culminar")
  
  
  
  '''
    # 1. importar dataset para crear las tablas de nuestro modelo_orm
    #Importo mis datos csv, paso path o uso el predeterminado
    carga = CargaDatos()
    carga.cargarDatosPrevios()

    #Una vez cargado los datos del dataset agregar dos nuevas empresas
    #TODO:armar dos empresas
    
    #Pasar las dos empresas por la totalidad de estados solicitados  
    
    #Presionar una tecla para culminar
    
  '''
  
  
if __name__ == '__main__':
  main() 
    
   
