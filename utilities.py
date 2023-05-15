import os
from colorama import Fore
red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET


def leer_archivo_base(path: str):
    ''' 
    Doc:
        target:
            se valida si el archivo existe en la ruta indicada y
            retorna una lista de cada linea o renglon
        params:
            path: str, se le pasa como parámetro la ruta del archivo del cual
            se desea leer la informacion.
    '''
    try:
        if os.path.isfile(path):  # valida si el archivo existe
            file = open(path, 'r', encoding="utf-8")
            lectura = file.read()
            file.close()
            # separa por linea cada comando SQL 21395617-18
            lista = lectura.split('\n')
            return lista
        else:
            os.system("cls")

            print(red, 'La ruta no pertenece a un archivo', freset)
            raise ValueError('La ruta no pertenece a un archivo')
            return False
    except Exception as err:
        return err


def equalizer(columnas1: str, lista2: list):
    '''
    Doc:
        target:
            igualar la cantidad de columnas del receptor en el resultado
        params:
            column1: str, contiene las columnas insertadas por el usuario
            column2: str, contiene las columnas definidas en el archivo de texto
    '''

    columnas1, len2 = int(columnas1), len(lista2)

    if columnas1 > len2:
        n = columnas1-len2
        for indice in range(n):
            del columnas1[indice]
    elif columnas1 < len2:
        n = len2-columnas1
        for indice in range(n):
            columnas1.append('columnaX'+str(indice))
    elif columnas1 == len2:
        print(green, "Listas de igual dimension", freset)
    else:
        pass


def save_file(text: str):  # función para agregar strings en el archivo resultado
    '''
    Doc:
        target:
            guardar la información o resultado en el archivo resultado.txt
        params:
            text: str, recibe el como parámetro la información para ser insertada en el archivo nuevo
    '''
    with open(f"./inbox/resultado.txt", "w", encoding="utf-8") as file:
        file.write(text)  # separa por salto de linea
