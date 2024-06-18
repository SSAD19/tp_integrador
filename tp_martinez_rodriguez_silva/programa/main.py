from tp_martinez_rodriguez_silva.programa.importar_datos import *
from modelo_orm import *

if __name__ == '__main__':
  
  
  # 1. importar dataset para crear las tablas de nuestro modelo_orm
  data = importar_datos()
  if data is False:
    exit()
  
  
