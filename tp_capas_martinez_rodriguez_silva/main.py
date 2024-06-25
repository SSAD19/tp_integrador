from sqlite3 import OperationalError
from  utils.db_obras import *
from models import empresas as em, area_responsable as ar, contrataciones as con 
from models import etapa_obra as eo, licitacion as li, obra as ob
from models import predio as pr, tipo_contratacion as tc, tipo_obra as to



  
def main():  
  
  db_sqlite = BaseDatos()
  
  db_sqlite.abrirConex()
  
  #falta etap_obra, tipo_obra, obra
  db_sqlite.crearTabla(em.Empresa, ar.AreaResponsable, con.Contratacion, li.Licitacion, pr.Predio, tc.TipoContratacion)
  
  
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
    
   
