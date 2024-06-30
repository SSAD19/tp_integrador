from negocio.gestionar_obras import * 
from peewee import *
from pandas import *
import asyncio


#funcion de limpieza más especifica de la data
def limpiar_principales_data(dataframe, columns:list):
      for i in columns:
        dataframe = GestionarObra.limpiar_datos(dataframe, i)
      return dataframe
   
#funciona perfecto, no tocar
async def cargando_datos_de_un_campo(dataframe, nombreColumna:str, campo:str, model=BaseModel,):
  
    listado = GestionarObra.datos_unique(dataframe, nombreColumna)
    
    for i in listado: 
        reg = {campo: i}
        await GestionarObra.cargar_datos_subclase(model, reg)

async def extraccion_Data(): 
    #pasamos el archivo csv a dataframe se paso por defecto, pero puede pasarse otro archivo
    data = GestionarObra.extraer_datos()
    
    #Iniciamos la limpieza de los datos migrados eliminando las columnas que no vamos a utilizar
    columnas=['imagen_1', 'imagen_2', 'imagen_3', 'imagen_4', 
            'beneficiarios', 'compromiso', 'destacada', 'ba_elige', 'link_interno', 'estudio_ambiental_descarga',
            'financiamiento', 'Unnamed: 36']  
  
    data = GestionarObra.eliminar_columnas(data, columnas)
    
    #Eliminamos los registros exportados con fallas en los campos que consideramos son excluyentes
    columnas_limpiar=[ 'nombre', 'nro_contratacion','expediente-numero']
    data = limpiar_principales_data(data, columnas_limpiar)
  
    #verificamos que hayan quedado las columnas necesarias
    GestionarObra.imprimir_data(data)
     
    #iniciamos con la carga de datos de las subtablas 
    await cargando_datos_de_un_campo(data, 'area_responsable','nombre_area', AreaResponsable)
    print('Cargando datos')
    await cargando_datos_de_un_campo(data, 'tipo', 'nombre', TipoObra)
    print('Cargando datos')
    await cargando_datos_de_un_campo(data, 'contratacion_tipo', 'nombre', TipoContratacion)
    print('Cargando datos')
    await cargando_datos_de_un_campo(data, 'etapa', 'nombre', EtapaObra)
    print('Cargando datos')
    await cargando_datos_de_un_campo(data, 'barrio', 'barrio', Predio)
    print('Cargando datos')
    
    
    data_empresa = data[['licitacion_oferta_empresa', 'cuit_contratista']]
    await cargando_datos_de_un_campo(data_empresa, 'licitacion_oferta_empresa', 'razon_social', Empresa)
        
    # print('continua la carga de datos, por favor, espere.') 
    # await GestionarObra.cargar_datos(data)


def cargar_data_subtabla_importante():
  EtapaObra.create(nombre='rescindido')
  
  EtapaObra.create(nombre='nuevo proyecto')
  print('nuevas etapas obras creadas')

#TODO:  PASAR TODO LO DE LAS ETAPAS
def pasar_por_etapas(obra:Obra):
  try:
    #En la vida real se solicitarian mediante input, preferiblemente por formularios en una interfaz web, escritorio o app móvil
    # Para propósitos de demostración, se crean datos ficticios o de ejemplo.
 
    obra.iniciar_contratacion()
  except Exception as e:  
    print(e) 

async def main(): 
  
    
    #Primer bloque creamos nuestra base de datos, conexión 
    GestionarObra.conectar_db()
        
    #Creo las tablas necesarias para mi DB desde mis modelos
    GestionarObra.mapear_orm(AreaResponsable, TipoObra, TipoContratacion, Predio, Empresa, Contratacion, Licitacion, EtapaObra, Obra)
 
    # #Extrae los datos del dataSet 
    await extraccion_Data()
    print('data completamente cargada')
    
    cargar_data_subtabla_importante()
    
    
    # obra_nueva= GestionarObra.nueva_obra() 
    
    # tipo = TipoContratacion.select().where(TipoContratacion.nombre=='Obra Publica')  
    # contratacion_data ={'nro_contratacion' : '1298/2024','tipo_contratacion':tipo,}
    # obra_nueva.iniciar_contratacion(contratacion_data)
    
      
    # empresa = Empresa.create(razon_social='Cualquiera SA')
    # monto = 17865009.00
    # obra_nueva.adjudicar_obra(empresa, monto)
    
    
    obra_hardcodeada = GestionarObra.nueva_obra_hardcodeada()
    
    if obra_hardcodeada != None:
      tipo = TipoContratacion.select().where(TipoContratacion.nombre=='Contratacion Menor')  
      contratacion_data ={'nro_contratacion' : '1299/2024','tipo_contratacion':tipo,}
      obra_hardcodeada.iniciar_contratacion(contratacion_data)
      
      empresa = Empresa.create(razon_social='another + SA')
      monto = 985421859.00
      obra_hardcodeada.adjudicar_obra(empresa, monto)
    else: 
      print('No se pudo crear la obra')
   
    
    
    GestionarObra.cerrarConex()
    input("presione enter para culminar")



 
 
if __name__ == '__main__':
  try:
    asyncio.run(main()) 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   

