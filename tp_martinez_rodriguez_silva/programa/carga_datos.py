from importar_datos import *
from modelo_orm import *


def cargarDatosPrevios(): 
  #Importo mis datos csv, paso path o uso el predeterminado
  datos_obras_urbanas = importar_datos()
  
  #chequeamos nombres columnas
  imprimir_data(datos_obras_urbanas)
  
  #cargar Empresas 
  datos_obras_urbanas = eliminar_vacios(datos_obras_urbanas, 'licitacion_oferta_empresa')
  Empresas = datos_unique(datos_obras_urbanas, 'licitacion_oferta_empresa')
  
  for i in Empresas: 

    try: 
      if datos_obras_urbanas['licitacion_oferta_empresa'].str.contains(i):
        cuit = datos_obras_urbanas['cuit_contratista']
      else:
        cuit = None
        
      Empresa.create(licitacion_oferta_empresa = i,
                     cuit_contratista =cuit)
      
    except DatabaseError as e: 
      print(f"Error al crear empresa {e}")
      
    except Exception as e:
      print(f"Error al crear empresa {e}")