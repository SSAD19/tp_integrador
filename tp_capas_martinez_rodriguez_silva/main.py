from dao.empresa_dao import EmpresaDao
from utils.db_obras import *
from models import empresas as em, area_responsable as ar, contrataciones as con, licitacion as li, predio as pr
from dao.dao import *
  
def main():  
  
  db_sqlite = BaseDatos()
  db_sqlite.abrirConex()
  
  
  #TODO:falta etap_obra, tipo_obra, obra
  db_sqlite.crearTabla(em.Empresa, ar.AreaResponsable, con.Contratacion, li.Licitacion, pr.Predio)
  print(db_sqlite.db.get_tables())
  
  try: 
    empresa_dao = EmpresaDao()
    #empresa_dao.crearModelo(razon_social="Mi caminito S.A.", cuit=30123456779, activa=True)
    lista_empresas = empresa_dao.traerTodos()
    for i in lista_empresas: print(i.razon_social, i.cuit)
      
  except Exception as e:
    print("error:", e)
 
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
    
   
