import os
from colorama import Back, Fore

red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET

def leer_archivo_base(ruta_archivo):
    ''' Documentacion:
    - se le pasa como parametro la ruta del archivo del cual se desea leer la informacion.
    - se valida si el archivo existe en la ruta indicada
    '''
    try:
        if os.path.isfile(ruta_archivo):  # valida si el archivo existe
            file = open(ruta_archivo, 'r', encoding="utf-8")
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

def equalizer(columnas1, lista2):
    ''' Documentacion:
    - column1, contiene las columnas insertadas por el usuario
    - column2, contine las columnas definidas en el archivo de texto
    - el objetivo final de esta funcion es tener el mismo numero de columnas insertadas por el usuario y en el archivo
    '''
    len1, len2 = len(columnas1), len(lista2)
    if len1 > len2:
        n = len1-len2
        for indice in range(n):
            del columnas1[indice]
    elif len1 < len2:
        n = len2-len1
        for indice in range(n):
            columnas1.append('columnaX'+str(indice))
    elif len1 == len2:
        print(green, "Listas de igual dimension", freset)
    else:
        pass


def save_file(text):  # funcion para agragar strings en el archivo resultado
    ''' Documentacion:
    -  recibe el como parametro la informacion para ser insertada en el archivo nuevo
    - el nombre del archivo por defecto que se generara se llamara resultado.txt
    '''
    file = open("resultado.txt", "a", encoding="utf-8")
    file.write(text)  # separa por salto de linea
    file.close()