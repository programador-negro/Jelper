# modulo que cambia el color de la fuente por consola o terminal
import os  # para borrar la inforamcion impresa en la terminal o consola
# para copiar las variables de algunas funciones
from colorama import Back, Fore, init
from excel_manager import excel_insert, excel_update, excel_xml
from utilities import save_file
from text_manager import transportar_aJson2_redAmor, transport_delete, transport_insert, transport_update
import logging
from config_manager import ConfigManager
import json

logging.info('Stating Program')


init()  # inicializador de colores de terminal

red = Fore.RED 
green = Fore.GREEN 
blue = Fore.BLUE 
yellow = Fore.YELLOW 
freset = Fore.RESET

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')


config = ConfigManager(config_path).get_config()

numbers: set = set(json.loads(config['data_sources'].get('numbers')))
statements: set = set(json.loads(config['data_sources'].get('sql_statements')))
emoji_bug: str = config['emojis'].get('bug')
emoji_irritate: str = config['emojis'].get('irritate')

txt_filename: str = config['data_sources'].get('txt_filename')
xlsx_filename: str = config['data_sources'].get('xlsx_filename')

# File path to save results
inbox_path: str = os.path.join( os.path.dirname(__file__) , 'inbox')

# File path to read sources
outbox_path: str = os.path.join( os.path.dirname(__file__) , 'outbox')

def inicio():
    '''
    Inicio del programa
    '''

    while True:
        print(f'''
                {Fore.BLACK+Back.WHITE}{emoji_bug} \
                YO TE AYUDO  \
                {emoji_bug}{Back.RESET+Fore.RESET}

        #️⃣  Select 0ption:

        1️⃣  Txt to INSERT
        2️⃣  Txt to UPDATE
        3️⃣  Txt to DELETE
        4️⃣  transport to JSON red Amor
        5️⃣  Excel to INSERT
        6️⃣  Excel to UPDATE
        7️⃣  Excel to XML

        [{red}*{freset}] - GO OUT \n''')

        opt = input("answer: ")

        match opt:
            case '1':
                transport_insert(numbers=numbers, statements=statements, inbox_path=inbox_path, outbox_path=outbox_path, filename=txt_filename)
            case '2':
                transport_update(numbers, statements, inbox_path=inbox_path, outbox_path=outbox_path, filename=txt_filename)
            case '3':
                transport_delete()
            case '4':
                transportar_aJson2_redAmor()
            case '5':
                excel_insert(numbers, statements, save_file, inbox_path=inbox_path, outbox_path=outbox_path, filename=xlsx_filename)
            case '6':
                excel_update(numbers, statements, save_file, inbox_path=inbox_path, outbox_path=outbox_path, filename=xlsx_filename)
            case '7':
                excel_xml()
            case '*':
                print(Fore.BLUE+"Bye!"+Fore.RESET)
                break
            case _:
                os.system("cls")  # borra informacion de la consola o terminal
                print(
                    Fore.RED, f'\n{emoji_irritate} ¡OPCION INCORRECTA!', Fore.RESET)


# ----------- ejecucion ------------
if '__main__' == __name__:
    inicio()
