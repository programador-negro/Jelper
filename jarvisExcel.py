import pandas as pd # para lectura de la informacion de Excel
from copy import deepcopy
from datetime import datetime
from colorama import init, Fore, Back 
import os

def excelUpdate():
    try:
        dirFile = input('\U0001F600 Ingrese la ruta del archivo: ')
        hoja = input("Nombre de hoja: ")
        tabla = input("Nombre de tabla: ")

        # -------------
        # # Imprimir hojas del Archivo.
        # xl = pd.ExcelFile(dirFile)
        # print(xl.sheet_names)

        dataFrame = pd.read_excel(dirFile, sheet_name=hoja)
        columnas = list(dataFrame.columns.values)
        query = f"UPDATE {tabla} SET "
        comando = deepcopy(query)
        tiempo_inicio = datetime.now()

        whereConditions = list()
        contenido = str()
        for index in range(len(dataFrame)):
            # convierte cada fila de excel en una lista
            values = list(dataFrame.loc[index])

            # itera dos variables, las columnas y los valores de cada celda en la fila
            for key, value in zip(columnas, values):
                if values.index(value) == 0:
                    whereConditions.append(f" WHERE {key} = {value}")
                else:
                    if value in numeros_string or value in predeterminados:
                        comando += f"{key} = {value},"
                    else:
                        comando += f"{key} = '{value}',"

            comando = comando[:-1]  # Elimina la ultima coma del String
            comando += whereConditions[-1]
            comando += ";\n"  # salto de linea
            contenido += comando
            print(comando)

            comando = query
        addend_arch(contenido)
        tiempo_final = datetime.now()

        print(Fore.GREEN+"\tTIEMPO DE EJECUCION")
        print("\tInicio: ", tiempo_inicio)
        print("\tFin: ", tiempo_final)
        print("\t - - - - - - -")
        print("\t", tiempo_final-tiempo_inicio, Fore.RESET)

    except Exception as ex:

        print(f" \U0000274C {red}ERROR:{freset} " + str(ex))
        # exc_type, exc_obj, exc_tb = sys.exc_info()
        # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # print(exc_type, fname, exc_tb.tb_lineno)

# transformar datos de Excel a comandos INSERT SQL


def excelInsert():
    dirFile = input('ingrese la ruta del archivo: ')
    hoja = input("Nombre de hoja: ")
    tabla = input("Nombre de tabla: ")

    # -------------
    # # Imprimir hojas del Archivo.
    # xl = pd.ExcelFile(dirFile)
    # print(xl.sheet_names)

    dataFrame = pd.read_excel(dirFile, sheet_name=hoja)

    columnas = list(dataFrame.columns.values)

    query = f"INSERT INTO {tabla}("
    for colum in columnas:
        query += f"`{colum}`,"
        
    query = query[:-1]
    query += ") VALUES("

    comando = deepcopy(query)

    tiempo_inicio = datetime.now()
    print("\t", tiempo_inicio)

    for index in range(len(dataFrame)):
        # Obtiene los valores de una fila los combierte en una lista para luego ser recorrido
        values = list(dataFrame.loc[index])
        for value in values:  # recorre la fila
            if value in numeros_string or value in predeterminados:
                comando += f"{value},"
            else:
                comando += f"'{value}',"

        comando = comando[:-1]  # Elimina la ultima coma del String
        comando += ");\n"  # salto de linea
        addend_arch(comando)
        print(comando)
        # addend_arch(comando)
        comando = query

    tiempo_final = datetime.now()
    print("\t", tiempo_final)
