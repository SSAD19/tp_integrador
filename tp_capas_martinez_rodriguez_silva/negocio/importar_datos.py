#  .\dataset\observatorio-de-obras-urbanas.csv path cvs
import pandas as pd
import numpy as np


my_dataframe = ".\dataset\observatorio-de-obras-urbanas.csv"
   
#Función para ingresar al  archivo a exportar            
def importar_datos(dataframe = my_dataframe):
    try:
        data = pd.read_csv(dataframe, sep=",")
        return data
    
    except FileNotFoundError as e:
        print("Error al conectar con el dataset.", e)
        return False
    
    except Exception as e: 
        print("Error al importar dataset. ", e)
        return False

#Funcion para mostrar la estructura de mi tabla
def imprimir_data(data):
    #en caso de haber algún error en la data retorna sin hacer nada
    # guarda
    if data is False: return
    
    #Imprimir nombres para confirmar datos de columnas
    print(data.columns)
    #Imprimir cantidad total de datos (?)
    print(data.count())
    
    #TODO: Chequear como se ven esos datos por consola 
    
    

#Funciones para eliminar los campos vacios 
def eliminar_vacios(data, nombreColumna:str):
    if data is False: return
    
    try:
        return data.dropna(subset=[f'{nombreColumna}'], axis =0, inplace= True)
       
    except Exception as e: 
        print("Erros, no se pudo ingresar limpiar los registros. ", e)
        return
    
#función para eliminar datos repetidos 
def datos_unique(data, nombreColumna:str):
    if data is False: return
    try:
        return list(data[f'{nombreColumna}'].unique())
    
    except Exception as e:
        print("Erros, no se pudo unificar el listado. ", e)
        return