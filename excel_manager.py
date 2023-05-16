import pandas as pd  # para lectura de la informacion de Excel
from copy import deepcopy
from decorators import total_time_execution
import os

@total_time_execution
def excel_update(numbers: set, statements: set, save_on_file, inbox_path, outbox_path, filename):
    '''
    take excel file records and convert them into SQL Update query one by one
    '''

    numeros_string = numbers
    predeterminados = statements

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
        save_on_file(contenido)

    except Exception as ex:

        print(f"\U0000274C ERROR: {ex}")
    finally:
        print("ERROR: No fue posible seguir ejecutando el programa.")


# transformar datos de Excel a XML
@total_time_execution
def excel_xml():
    '''
    take excel file records and convert them into XML code, one by one
    '''

    try:
        dirFile = input('\U0001F600 Ingrese la ruta del archivo: ')
        hoja = "Hoja1"

        dataFrame = pd.read_excel(dirFile, sheet_name=hoja)
        columnas = list(dataFrame.columns.values)
        query = f""
        comando = deepcopy(query)

        contenido = str()
        for index in range(len(dataFrame)):
            values = list(dataFrame.loc[index])

            for key, value in zip(columnas, values):
                if values.index(value) == 0:
                    comando += f'<registro {key}="{value}" '
                else:
                    comando += f'{key}="{value}" '
            comando += "/>\n"  # salto de linea
            contenido += comando
            comando = query
        print("-<transaccion_siebel> " +
              "-<TT> " +
              "-<SiebelMessage> " +
              "-<psRegistro>" +
              contenido +
              "</psRegistro>"
              "</SiebelMessage>" +
              "</TT>" +
              "</transaccion_siebel>"
              )

    except Exception:
        print(" 🚨 ERROR: " + Exception)


# transformar datos de Excel a comandos INSERT SQL
@total_time_execution
def excel_insert(numbers: str, statements: str, save_on_file, inbox_path, outbox_path, filename):
    '''
    take excel file records and convert them into SQL Insert query one by one
    '''

    try:
        numeros_string = numbers
        predeterminados = statements
        
        file_name = input('ingrese la nombre del archivo: ')
        hoja = input("Nombre de hoja: ")
        tabla = input("Nombre de tabla: ")

        # -------------
        # # Imprimir hojas del Archivo.
        # xl = pd.ExcelFile(dirFile)
        # print(xl.sheet_names)

        dataFrame = pd.read_excel(os.path.join(outbox_path, file_name), sheet_name=hoja)

        columnas = list(dataFrame.columns.values)

        query = f"INSERT INTO {tabla}("
        for colum in columnas:
            query += f"`{colum}`,"

        query = query[:-1]
        query += ") VALUES("

        comando = deepcopy(query)

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

            save_on_file(comando, inbox_path, filename)
            
            print(comando)
            
            comando = query

    except Exception:
        print(f"ERROR: {Exception}")

    finally:
        print("ERROR: No fue posible seguir ejecutando el programa")
