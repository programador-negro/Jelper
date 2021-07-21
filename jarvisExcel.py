import pandas as pd
from copy import deepcopy
from datetime import datetime
from colorama import init, Fore, Back 
import os
def Excel_aInsert():
    dirFile = input('ingrese la ruta del archivo: ')
    hoja = input("Nombre de hoja: ")
    tabla = input("Nombre de tabla: ")

    dataFrame = pd.read_excel(dirFile, sheet_name=hoja)
    # print(list(dataFrame.columns.values)) # imprime el nombre de las columnas
    # print(list(dataFrame["Salario"]))
    columnas = list(dataFrame.columns.values)

    query = f"INSERT INTO {tabla}("
    for colum in columnas:    
        query += f"{colum},"
    query = query[:-1]
    query += ") VALUES("

    comando = deepcopy(query)

    tiempo_inicio = datetime.now()
    print("\t",tiempo_inicio)

    for index in range(len(dataFrame)):
        values = list(dataFrame.loc[index])
        for value in values:
            comando += f"'{value}',"
        comando = comando[:-1]
        comando+=");\n"
        print(comando)
        # addend_arch(comando)
        comando = query
        
    tiempo_final = datetime.now()
    print("\t",tiempo_final)

def excel_update():
    print(f'''
    |--------{red} ADVERTENCIA {freset}--------|
    La primera columna de donde se 
    toman los datos hace referencia 
    la columna condicional de WHERE
    |-----------------------------|
    ''')
    ruta_archivo = input('ingrese la ruta del archivo: ')
    
