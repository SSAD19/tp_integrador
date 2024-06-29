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


#Primera pàrte funciona, falta asignar cuit
async def cargar_datos_empresa(data_empresa):

      #carga de razones sociales unique: 
      await cargando_datos_de_un_campo(data_empresa, 'licitacion_oferta_empresa', 'razon_social', Empresa)
      
      lista_empresas = Empresa()
      lista_empresas = lista_empresas.select()
      print(lista_empresas)
      
      #TODO: lISTA DE CUITS DONDE LA COLUMNA DE MI DATAFRAME COINCIDE CON MI LISTADO DE EMPRESAS
     
    
async def main(): 
  
    
    #Primer bloque creamos nuestra base de datos, conexión 
    GestionarObra.conectar_db()
    
    #Creo las tablas necesarias para mi DB desde mis modelos
    GestionarObra.mapear_orm(AreaResponsable, TipoObra, TipoContratacion, Predio, Empresa, Contratacion, Licitacion, EtapaObra, Obra)
 
    #Extraigo los datos del dataSet .- t
    # rae un path por defecto, pero puede ingresarse para reutilizacion en otros casos
    data = GestionarObra.extraer_datos()
    
      #Iniciamos la limpieza de los datos migrados eliminando las columnas que no vamos a utilizar
    columnas=['plazo_meses', 'imagen_1', 'imagen_2', 'imagen_3', 'imagen_4', 
            'beneficiarios', 'compromiso', 'destacada', 'ba_elige', 'link_interno', 'estudio_ambiental_descarga',
            'financiamiento', 'Unnamed: 36', 'comuna']  
    data = GestionarObra.eliminar_columnas(data, columnas)
    print(len(data))
    
    columnas_limpiar=[ 'nombre', 'nro_contratacion','expediente-numero']
    data = limpiar_principales_data(data, columnas_limpiar)
    
    print(len(data))
    GestionarObra.imprimir_data(data)
     
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
    await cargar_datos_empresa(data_empresa)
    
    lista_empresas = Empresa.select().where(Empresa.id.between(1, 5))
    for empresa in lista_empresas:
        print(empresa, empresa.razon_social)
    
    print('continua la carga de datos, por favor, espere.') 
    await GestionarObra.cargar_datos(data)
    
    print('data correctamente cargada.')
    
    
    
    
    GestionarObra.cerrarConex()
    input("presione enter para culminar")




 
if __name__ == '__main__':
  try:
    asyncio.run(main()) 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   

