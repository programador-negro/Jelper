from utilities import leer_archivo_base
from utilities import save_file
from utilities import equalizer
from decorators import total_time_execution
from colorama import Fore, init
from copy import deepcopy
import os

init()  # inicializador de colores de terminal

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
freset = Fore.RESET


@total_time_execution  # calcula el tiempo de ejecucion de la funcion
def transport_insert(numbers: set, statements: set, path_param: str = None, table_param: str = None, columns_param: str = None, inbox_path, outbox_path, filename):
    ''' 
    DocString
        target:
            transforma los datos a comandos INSERT para luego ser usados en MySQL
        params:
            numbers: list, lista de números que deben ser convertidos a tipo entero
            statements: list, lista de palabras reservadas de SQL que no deben interpretarse como strings
    '''

    try:
        ruta_archivo: str = input(
            'ingrese la ruta del archivo: ') if path_param == None else path_param
        lineaSeparada = leer_archivo_base(ruta_archivo)
        comandoLargo: str = ""
        if lineaSeparada:
            tabla: str = input(
                'Tabla: ') if table_param == None else table_param
            columnas: str = input('Columnas: ').split(
            ) if columns_param == None else columns_param
            comando: str = f"INSERT INTO {tabla}("

            # toma el numero de columnas para comparar con el numero de valores a ingresar e igualar las columnas
            tempList = lineaSeparada[0].split(",")
            os.system("cls")
            equalizer(columnas, tempList)

            for colum in columnas:
                # agrega las columnas ingresadas
                comando += f"{colum.strip()},"

            # borra la ultima coma que sobra del string, la cual genera el for anterior
            comando = comando[:-1]
            comando += ") VALUES("

            ini = deepcopy(comando)  # copia la variable 'comando'

            for item in lineaSeparada:
                elem_sep = item.split(',')
                for one_item in elem_sep:
                    # valida si alguno de los campos son de tipo numero para colocarlos sin comillas
                    if one_item in numbers or one_item in statements:
                        comando += f" {one_item.strip()},"
                    else:
                        comando += f" '{one_item.strip()}',"

                comando = comando[:-1]
                comando += ");\n"

                comandoLargo += comando
                comando = ini
        save_file(comandoLargo, inbox_path=inbox_path, filename=filename)
    except Exception as ex:
        print(f"ERROR: {ex}")
    finally:
        print("<< No fue posible seguir ejecutando el programa >>")


# transforma los datos a comandos INSERT para luego ser usados en MySQL
@total_time_execution
def transport_update(numbers: set, statements: set, inbox_path, outbox_path, filename):
    os.system("cls")
    print(f'''
    |--------{red} ADVERTENCIA {freset}--------|
    La primera columna de donde se 
    toman los datos hace referencia 
    la columna condicional de WHERE
    |-----------------------------|
    ''')
    try:
        ruta_archivo = input(f'{yellow}Ingrese la ruta del archivo: {freset}')
        lineaSeparada = leer_archivo_base(ruta_archivo)
        comandoLargo = ""
        if lineaSeparada:
            tabla, columnas = input('Tabla: '),  input('Columnas: ').split()

            comando = f"UPDATE {tabla} SET "

            # toma el numero de columnas para comparar con el numero de valores a ingresar e igualar las columnas
            tempList = lineaSeparada[0].split(",")
            os.system("cls")
            equalizer(columnas, tempList)

            ini = deepcopy(comando)  # copia la variable 'comando'

            for item in lineaSeparada:
                elem_sep = item.split(',')

                for inx in range(len(elem_sep)):
                    # Evita colocar la columna condicional despues de WHERE dentro de SET
                    if elem_sep.index(elem_sep[inx]) != 0:
                        if elem_sep[inx] in numbers or elem_sep[inx] in statements:
                            comando = f"{columnas[inx].strip()}={elem_sep[inx].strip()},"
                        else:
                            comando += f"{columnas[inx].strip()}='{elem_sep[inx].strip()}',"
                    else:
                        continue

                comando = comando[:-1]
                comando += f" WHERE {columnas[0].strip()}='{elem_sep[0].strip()}';\n"

                comandoLargo += comando
                comando = ini
        save_file(comandoLargo, inbox_path=inbox_path, filename=filename)

    except Exception as ex:
        print(f"ERROR: {ex}")
    finally:
        print("<< No fue posible seguir ejecutando el programa >>")


@total_time_execution
def transport_delete(numbers: set, statements: set, inbox_path, outbox_path, filename):  # transforma los datos a comandos DELETE para luego ser usados en MySQL
    os.system("cls")
    print(f'''
    |-------- {red}ADVERTENCIA{freset} --------|
    El programa solo toma la primera
    columna para ser definida despues
    del WHERE, las demas columnas no
    seran tomadas en cuenta
    |-----------------------------|
    ''')
    try:
        ruta_archivo: str = input('Ingrese la ruta del archivo: ')
        lineaSeparada = leer_archivo_base(ruta_archivo)
        comandoLargo: str = ""
        if lineaSeparada:
            tabla = input('Tabla: ')
            columnas = input('Columna: ').split()
            columnas = columnas[0]
            comando = f"DELETE FROM {tabla} WHERE {columnas}= '"

            ini = deepcopy(comando)  # copia la variable 'comando'
            os.system("cls")

            for item in lineaSeparada:
                comando += f"{item[0].strip()}';\n"
                comandoLargo += comando
                comando = ini
        save_file(comandoLargo, inbox_path=inbox_path, filename=filename)

    except Exception as ex:
        print(f"ERROR: {ex}")
    finally:
        print("<< No fue posible seguir ejecutando el programa >>")


@total_time_execution
def transportar_aJson2_redAmor(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
    ''' Documentacion:
    - El proposito de esta funcion es generar los comandos INSERT SQL de la informacion enviada por cliente mediante Tickets de Seus.
    - la infomacion enviada por cliente llega en archivo de Excel, la columnas deben ordenarse en el orden del DICCIONARIO de esta funcion.
    - la informacion debe ser convertida en un archivo de texto separando los campos por coma (,).
    - proceder a ejecutar esta funcion y adjuntar la ruta donde se encuentra el archivo de texto.

    - - - Query resultado para cada fila del archivo de texto de ejemplo:  - - - 

    INSERT INTO db_consulta_red_de_amor_empresarial("created_at","created_by_id","updated_at","updated_by_id","deleted","form_id","managementTime","status","currentLevel","valuesJSON") 
    VALUES(
        '2020-11-10 07:30:59.394432-05',
        187,
        '2020-11-10 07:30:59.394432-05',
        187,
        false,
        3,
        0,
        'joined',
        'gestion',

    # Todo lo siguiente es un String de la columnas valuesJSON
        '{"tarifa":"La asignada",
        "negocio":"Grandes Empleadores",
        "nit_empresa":811025289,
        "tipo_de_persona":"Población específica",
        "telefono_trabajador":3187352293,
        "nombre_de_la_empresa":"Novaventa S.A.S",
        "nombre_del_trabajador":"YESICA GIRALDO GOMEZ",
        "#_documento_del_trabajador":1036398321,
        "tipo_documento_del_trabajador":"cc"}' );
    '''
    try:
        diccionario = {
            "Documento": "",
            "Estado": "",
            "Fecha": "",
            "CreadoPor": "",
            "TipoMensaje": "",
            "Cis": "",
            "Nombre": "",
            "Telefono": "",
            "Correo": "",
            "Mensaje": ""}

        ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
        lineaSeparada = leer_archivo_base(ruta_archivo)
        for item in lineaSeparada:
            elem_sep = item.split(',')

            diccionario["nit_empresa"] = elem_sep[0].strip()
            diccionario["nombre_de_la_empresa"] = elem_sep[1].strip()
            diccionario["#_documento_del_trabajador"] = elem_sep[2].strip()
            diccionario["tipo_documento_del_trabajador"] = elem_sep[3].strip()
            diccionario["nombre_del_trabajador"] = elem_sep[4].strip()
            diccionario["telefono_trabajador"] = elem_sep[5].strip()
            diccionario["tarifa"] = elem_sep[6].strip()
            diccionario["negocio"] = elem_sep[7].strip()
            diccionario["tipo_de_persona"] = elem_sep[8].strip()

            queryX = 'INSERT INTO db_consulta_red_de_amor_empresarial("created_at", "created_by_id", "updated_at", "updated_by_id", "deleted", "form_id", "managementTime", "status", "currentLevel", "valuesJSON") VALUES('
            queryX += "'2020-11-10 07:30:59.394432-05'"
            queryX += ',187,'
            queryX += "'2020-11-10 07:30:59.394432-05'"
            queryX += ',187,false,3,0,'
            queryX += "'joined','gestion',"

            string = " '{"
            string += f'"tarifa":"{diccionario["tarifa"] }",'
            string += f'"negocio":"{diccionario["negocio"]}",'
            string += f'"nit_empresa":{diccionario["nit_empresa"]},'
            string += f'"tipo_de_persona":"{diccionario["tipo_de_persona"]}",'
            string += f'"telefono_trabajador":{diccionario["telefono_trabajador"]},'
            string += f'"nombre_de_la_empresa":"{diccionario["nombre_de_la_empresa"]}",'
            string += f'"nombre_del_trabajador":"{diccionario["nombre_del_trabajador"]}",'
            string += f'"#_documento_del_trabajador":{diccionario["#_documento_del_trabajador"] },'
            string += f'"tipo_documento_del_trabajador":"{diccionario["tipo_documento_del_trabajador"]}"'
            string += "}' "
            queryX += string + ');\n'
            save_file(queryX)
    except Exception as ex:
        print(ex)
    finally:
        print("<< No fue posible seguir ejecutando el programa >>")
