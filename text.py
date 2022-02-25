from utilities import leer_archivo_base as leerArchivoBase
from utilities import equalizer as igualador
from utilities import save_file as guardarEnArchivo
from colorama import Back, Fore, init
from decorators import total_time_execution
import os
from copy import deepcopy  


init()  # inicializador de colores de terminal
red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET 
@total_time_execution
def transport_insert(numerosStr, predeterminados):  # transforma los datos a comandos INSERT para luego ser usados en MySQL
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leerArchivoBase(ruta_archivo)
    comandoLargo = ""
    if lineaSeparada:
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split()
        comando = f"INSERT INTO {tabla}("

        # toma el numero de columnas para comparar con el numero de valores a ingresar e igualar las columnas
        tempList = lineaSeparada[0].split(",")
        os.system("cls")
        igualador(columnas, tempList)

        for colum in columnas:
            comando += f"{colum.strip()},"  # agrega las columnas ingresadas

        # borra la ultima coma que sobra del string, la cual genera el for anterior
        comando = comando[:-1]
        comando += ") VALUES("

        ini = deepcopy(comando)  # copia la variable 'comando'

        for item in lineaSeparada:
            elem_sep = item.split(',')
            for one_item in elem_sep:
                # valida si alguno de los campos son de tipo numero para colocarlos sin comillas
                if one_item in numerosStr or one_item in predeterminados:
                    comando += f" {one_item.strip()},"
                else:
                    comando += f" '{one_item.strip()}',"

            comando = comando[:-1]
            comando += ");\n"

            comandoLargo += comando
            comando = ini
    guardarEnArchivo(comandoLargo)

# convertir informacion de archivos de texto a sentencias UPDATE SQL

@total_time_execution
def transport_update(numerosStr, predeterminados):  # transforma los datos a comandos INSERT para luego ser usados en MySQL
    os.system("cls")
    print(f'''
    |--------{red} ADVERTENCIA {freset}--------|
    La primera columna de donde se 
    toman los datos hace referencia 
    la columna condicional de WHERE
    |-----------------------------|
    ''')
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leerArchivoBase(ruta_archivo)
    comandoLargo = ""
    if lineaSeparada:
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split()
        comando = f"UPDATE {tabla} SET "

        # toma el numero de columnas para comparar con el numero de valores a ingresar e igualar las columnas
        tempList = lineaSeparada[0].split(",")
        os.system("cls")
        igualador(columnas, tempList)

        ini = deepcopy(comando)  # copia la variable 'comando'

        for item in lineaSeparada:
            elem_sep = item.split(',')

            for inx in range(len(elem_sep)):
                # Evita colocar la columna condicional despues de WHERE dentro de SET
                if elem_sep.index(elem_sep[inx]) != 0:
                    if elem_sep[inx] in numerosStr or elem_sep[inx] in predeterminados:
                        comando = f"{columnas[inx].strip()}={elem_sep[inx].strip()},"
                    else:
                        comando += f"{columnas[inx].strip()}='{elem_sep[inx].strip()}',"
                else:
                    continue

            comando = comando[:-1]
            comando += f" WHERE {columnas[0].strip()}='{elem_sep[0].strip()}';\n"

            comandoLargo += comando
            comando = ini
    guardarEnArchivo(comandoLargo)

@total_time_execution
def transport_delete():  # transforma los datos a comandos INSERT para luego ser usados en MySQL
    os.system("cls")
    print(f'''
    |-------- {red}ADVERTENCIA{freset} --------|
    El programa solo toma la primera
    columna para ser definida despues
    del WHERE, las demas columnas no
    seran tomadas en cuenta
    |-----------------------------|
    ''')
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leerArchivoBase(ruta_archivo)
    comandoLargo = ""
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
    guardarEnArchivo(comandoLargo)

@total_time_execution
def transportar_aJson2_redAmor():  # transforma los datos a comandos INSERT para luego ser usados en MySQL
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
        lineaSeparada = leerArchivoBase(ruta_archivo)
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
            guardarEnArchivo(queryX)
    except Exception as ex:
        print(ex)
# - - - - Inicio de la ejecucion del programa - - - -
