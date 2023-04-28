# modulo que cambia el color de la fuente por consola o terminal
import os  # para borrar la inforamcion impresa en la terminal o consola
# para copiar las variables de algunas funciones
from colorama import Back, Fore, init
from excel_manager import excelInsert, excelUpdate, excelXML
from utilities import save_file
from text_manager import transportar_aJson2_redAmor, transport_delete as transportarDelete, transport_insert as transportarInsert, transport_update as transportarUpdate
import logger_manager, logging
# import logging

logging.info('Stating Program')

''' Pendientes para desarrollar:

- desarrollar la selección automática de hojas del archivo.
- desarrollar opción para abrir interfaz gráfica del programa, por medio de un commando.
- desarrollar una interfaz gráfica en c# para la lectura de archivos
- buscar la forma de ofuscar el codigo
- agregar modulo para insertar datos en base de datos
- agregar modulo para insertar datos desde una API JSON



'''
init()  # inicializador de colores de terminal
red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET

numbers: set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\t1\t',
                   '\t2\t', '\t3\t', '\t4\t', '\t5\t', '\t6\t', '\t7\t', '\t8\t', '\t9\t', '\t0\t'}
statements: list = {'null', 'NULL', 'Null',
                         'nUll', 'current_timestamp', 'CURRENT_TIMESTAMP'}


def inicio():
    while True:
        print(f'''
        {Fore.BLACK+Back.WHITE}\U0001F41E \
            YO TE AYUDO \
            \U0001F41E {Back.RESET+Fore.RESET}

        #️⃣  Select 0ption:

        1️⃣  Txt to INSERT
        2️⃣  Txt to UPDATE
        3️⃣  Txt to DELETE
        4️⃣  transport to JSON red Amor
        5️⃣  Excel to INSERT
        6️⃣  Excel to UPDATE
        7️⃣  Excel to XML

        [{red}*{freset}] - GO OUT
        ''')

        opt = input("R/: ")

        match opt:
            case '1':
                transportarInsert(numbers, statements)
            case '2':
                transportarUpdate(numbers, statements)
            case '3':
                transportarDelete()
            case '4':
                transportar_aJson2_redAmor()
            case '5':
                excelInsert(numbers, statements, save_file)
            case '6':
                excelUpdate(numbers, statements, save_file)
            case '7':
                excelXML()
            case '*':
                print(Fore.BLUE+"¡ADIOS!"+Fore.RESET)
                break
                quit()
            case _:
                os.system("cls")  # borra informacion de la consola o terminal
                print(Fore.RED, '\n💢 ¡OPCION INCORRECTA!', Fore.RESET)


# ----------- ejecucion ------------
if '__main__' == __name__:
    inicio()
