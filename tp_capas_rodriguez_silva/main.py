from negocio.gestionar_obras import * 
from peewee import *
from pandas import *



def cargando_dataframe_un_campo(dataframe, nombreColumna:str, campo:str, model=BaseModel,):
  
    listado = GestionarObra.datos_unique(dataframe, nombreColumna)
    
    for i in listado: 
        reg = {campo: i}
        GestionarObra.cargar_datos(model, reg)
   
    
def main(): 
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
      
#     cargando_dataframe_un_campo(data, 'area_responsable','nombre_area', AreaResponsable)
#     cargando_dataframe_un_campo(data, 'tipo', 'nombre', TipoObra)
#     cargando_dataframe_un_campo(data, 'contratacion_tipo', 'nombre', TipoContratacion)
#     cargando_dataframe_un_campo(data, 'etapa', 'nombre', EtapaObra)
#     cargando_dataframe_un_campo(data, 'barrio', 'barrio', Predio)
   
#    #cargando dato principal de empresa 
#    #TODO: NO CARGÓ!!!!
#     cargando_dataframe_un_campo(data, 'licitacion_oferta_empresa', 'razon_social', Empresa)
    
    #cragar por un for los cuit del dataframe que coincidan con la lista de empresas 
   
    #cargando dato principal de empresa 

   
   

    GestionarObra.cerrarConex()
    input("presione enter para culminar")
  
main()