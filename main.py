# modulo que cambia el color de la fuente por consola o terminal
import os  # para borrar la inforamcion impresa en la terminal o consola
import sys
# para copiar las variables de algunas funciones
from datetime import datetime
from colorama import Back, Fore, init
from decorators import total_time_execution
from excel import excelInsert, excelUpdate, excelXML
from utilities import leer_archivo_base as leerArchivoBase
from utilities import equalizer as igualador
from utilities import save_file as guardarEnArchivo
from text import transportar_aJson2_redAmor, transport_delete as transportarDelete, transport_insert as transportarInsert, transport_update as  transportarUpdate

''' Pendientes para desarrollar:

- crear formato para carga masiva de excel en red amor empresarial.
- desarrollar la selección automática de hojas del archivo.
- desarrollar opción para abrir interfaz gráfica del programa, por medio de un commando.
- desarrollar una interfaz gráfica en c# para la lectura de archivos
- agregar pruebas unitarias
- buscar la forma de ofuscar el codigo
- agregar modulo para insertar datos en base de datos




'''
init()  # inicializador de colores de terminal
red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET

numerosStr : list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\t1\t', '\t2\t', '\t3\t', '\t4\t', '\t5\t', '\t6\t', '\t7\t', '\t8\t', '\t9\t', '\t0\t']
predeterminados : list = ['null', 'NULL', 'Null', 'nUll', 'current_timestamp', 'CURRENT_TIMESTAMP']

def inicio():
    suitch = True
    while suitch == True:
        print(f'''
        {Fore.BLACK+Back.WHITE}\U0001F41E YO TE AYUDO \U0001F41E {Back.RESET+Fore.RESET}

        #️⃣ Select 0ption:

        1️⃣ - Txt to INSERT
        2️⃣ - Txt to UPDATE
        3️⃣ - Txt to DELETE
        4️⃣ - transport to JSON red Amor
        5️⃣ - Excel to INSERT
        6️⃣ - Excel to UPDATE
        7️⃣ - Excel to XML
        
        [{red}*{freset}] - GO OUT
        ''')
        opt = input("R/: ")
        if opt == '1':
            transportarInsert(numerosStr, predeterminados)
        elif opt == '2':
            transportarUpdate(numerosStr, predeterminados)
        elif opt == '3':
            transportarDelete()
        elif opt == '4':
            transportar_aJson2_redAmor()
        elif opt == '5':
            excelInsert(numerosStr, predeterminados, guardarEnArchivo)
        elif opt == '6':
            excelUpdate(numerosStr, predeterminados, guardarEnArchivo )
        elif opt == '7':
            excelXML()
        elif opt == '*':
            print(Fore.BLUE+"¡ADIOS!"+Fore.RESET)
            suitch = False
            quit()
        else:
            os.system("cls")  # borra informacion de la consola o terminal
            print(Fore.RED, '💢 ¡OPCION INCORRECTA!', Fore.RESET)


# ----------- ejecucion ------------
if '__main__' ==  __name__:
    inicio()
