from negocio.gestionar_obras import * 
from peewee import *
from pandas import *
import asyncio


#funciona perfecto, no tocar
async def cargando_dataframe_un_campo(dataframe, nombreColumna:str, campo:str, model=BaseModel,):
  
    listado = GestionarObra.datos_unique(dataframe, nombreColumna)
    
    for i in listado: 
        reg = {campo: i}
        await GestionarObra.cargar_datos(model, reg)


#en construcción:
async def cargar_datos_empresa(data_empresa):
    # Limpiar y obtener razones sociales únicas
    data_empresa_limpia = GestionarObra.limpiar_datos(data_empresa)
    razon_soc = GestionarObra.datos_unique(data_empresa_limpia, 'licitacion_oferta_empresa')
    print(len(data_empresa_limpia))
    
    data_unique = []
    
   
    data_unique = [data_empresa_limpia['licitacion_oferta_empresa'] == rz for rz in razon_soc] return data_unique=data_empresa_limpia
    print(data_unique)
    print(len(data_unique))
    
    
    '''
    data_empresa_limpia = GestionarObra.limpiar_datos(data_empresa)
    razon_soc = GestionarObra.datos_unique(data_empresa_limpia, 'licitacion_oferta_empresa')

    data_unique = []

    # Inicializar un diccionario para almacenar datos únicos
    datos_unicos_dict = {}

    # Recorrer la lista de razones sociales
    for rz in razon_soc:
        # Filtrar data_empresa_limpia por la razón social actual
        empresa_data = data_empresa_limpia[data_empresa_limpia['licitacion_oferta_empresa'] == rz]

        # Si hay datos para la razón social actual
        if not empresa_data.empty:
            # Obtener los valores únicos de 'cuit' para la razón social actual
            cuits_unicos = empresa_data['cuit_contratista'].unique()

            # Recorrer los CUITs únicos
            for cuit in cuits_unicos:
                # Si el CUIT no existe en el diccionario, agregar una nueva entrada
                if cuit not in datos_unicos_dict:
                    datos_unicos_dict[cuit] = {
                        'licitacion_oferta_empresa': rz,
                        'cuit': cuit
                    }

    # Convertir el diccionario en una lista de diccionarios
    for cuit_data in datos_unicos_dict.values():
        data_unique.append(cuit_data)

    print(data_unique)
    
    '''
    
    
    
    
    
    
    for i in data_unique: 
      reg ={'razon_social':i['licitacion_oferta_empresa'],'cuit':i['cuit_contratista']}
      await GestionarObra.cargar_datos(Empresa, reg)
  
   
    
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
    GestionarObra.imprimir_data(data)
     
    # await cargando_dataframe_un_campo(data, 'area_responsable','nombre_area', AreaResponsable)
    # print('Cargando datos')
    # await cargando_dataframe_un_campo(data, 'tipo', 'nombre', TipoObra)
    # print('Cargando datos')
    # await cargando_dataframe_un_campo(data, 'contratacion_tipo', 'nombre', TipoContratacion)
    # print('Cargando datos')
    # await cargando_dataframe_un_campo(data, 'etapa', 'nombre', EtapaObra)
    # print('Cargando datos')
    # await cargando_dataframe_un_campo(data, 'barrio', 'barrio', Predio)
    # print('Cargando datos')
    

    data_empresa = data[['licitacion_oferta_empresa', 'cuit_contratista']]
    await cargar_datos_empresa(data_empresa)
    
    GestionarObra.cerrarConex()
    input("presione enter para culminar")



'''
    # data_empresa = data[['licitacion_oferta_empresa', 'cuit_contratista']]
    
    # data_empresa = GestionarObra.limpiar_datos(data_empresa)
    # razon_social = GestionarObra.datos_unique(data_empresa, 'licitacion_oferta_empresa')

    # # empresa = Empresa()
    # try:
      
    #   for rz in razon_social:
        
    #       rows = data_empresa[data_empresa['licitacion_oferta_empresa'] == rz]
    #       razon= rows.iloc[0]['licitacion_oferta_empresa'] 
    #       cuit = rows.iloc[0]['cuit_contratista'] 
    #       empresa = {razon_social:razon, cuit:cuit}
    #       GestionarObra.cargar_datos(Empresa, empresa)
          
    # except Exception as e:
    #     print("Error al cargar los datos", e) '''



 
if __name__ == '__main__':
  try:
    asyncio.run(main()) 
  
  except ModuleNotFoundError as e:
    print("Falló la importación de módulos, comuníquese con el desarrollador") 
  
  except Exception as e:
    print("Error:", e)
   

