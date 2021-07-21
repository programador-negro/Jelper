from colorama import init, Fore, Back # modulo que cambia el color de la fuente por consola o terminal
from datetime import datetime
import os # para borrar la inforamcion impresa en la terminal o consola
from copy import deepcopy # para copiar las variables de algunas funciones
from datetime import datetime
import pandas as pd # para lectura de la informacion de Excel
import sys

''' Pendientes para desarrollar:

- crear formato para carga masiva de excel en red amor empresarial.
- desarrollar la seleccion automatica de hojas del archivo.
'''
init() # inicializador de colores
red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET

numeros_string = ['1','2','3','4','5', '6','7','8','9','0',
'\t1\t','\t2\t','\t3\t','\t4\t','\t5\t','\t6\t','\t7\t','\t8\t','\t9\t','\t0\t']

predeterminados = ['null','NULL','Null','nUll','current_timestamp','CURRENT_TIMESTAMP']


# - - - - -  leer archivo por la ruta o el Path- - - - - - 
def leer_archivo_base(ruta_archivo):
    ''' Documentacion:
    - se le pasa como parametro la ruta del archivo del cual se desea leer la informacion.
    - se valida si el archivo existe en la ruta indicada
    '''
    try:
        if os.path.isfile(ruta_archivo): # valida si el archivo existe
            file = open(ruta_archivo,'r', encoding="utf-8")
            lectura  = file.read()
            file.close()
            lista = lectura.split('\n') # separa por linea cada comando SQL 21395617-18
            return lista
        else:
            os.system("cls")
            
            print(red,'La ruta no pertenece a un archivo',freset)
            raise ValueError('La ruta no pertenece a un archivo')
            return False
    except Exception as err:
        return err

# - - - - - igualar columnas al momento de crear los query string - - - - - - -
def igualador(columnas1, lista2):
    ''' Documentacion:
    - column1, contiene las columnas insertadas por el usuario
    - column2, contine las columnas definidas en el archivo de texto
    - el objetivo final de esta funcion es tener el mismo numero de columnas insertadas por el usuario y en el archivo
    '''
    len1, len2 = len(columnas1), len(lista2)
    if len1>len2:
        n = len1-len2
        for indice in range(n):
            del columnas1[indice]
            #print(green,"igualadas",freset) 
    elif len1<len2:
        n = len2-len1
        for indice in range(n):
            columnas1.append('columnaX'+str(indice))
            #print(green,"igualadas",freset)
    elif len1==len2:
        print(green,"Listas de igual dimension",freset)
    else:
        pass
#- - - - - Generar archivo que recive la informacion - - - - - -
def addend_arch(text): # funcion para agragar strings en el archivo resultado
    ''' Documentacion:
    -  recibe el como parametro la informacion para ser insertada en el archivo nuevo
    - el nombre del archivo por defecto que se generara se llamara resultado.txt
    '''
    file = open("resultado.txt","a",encoding="utf-8")
    file.write(text) # separa por salto de linea
    file.close()

#---- Lectura de archivos EXCEL------------------- 

# transformar datos de Excel a comandos UPDATE SQL
def Excel_aUpdate():
    try:
        dirFile = input('\U0001F600 Ingrese la ruta del archivo: ')
        hoja = input("Nombre de hoja: ")
        tabla = input("Nombre de tabla: ")

        #-------------
        # # Imprimir hojas del Archivo.
        # xl = pd.ExcelFile(dirFile)
        # print(xl.sheet_names)
    
        dataFrame = pd.read_excel(dirFile, sheet_name=hoja)
        columnas = list(dataFrame.columns.values)
        query = f"UPDATE {tabla} SET "
        comando = deepcopy(query)
        tiempo_inicio = datetime.now()

        
        whereConditions = list()
        contenido=str()
        for index in range(len(dataFrame)):
            values = list(dataFrame.loc[index]) # convierte cada fila de excel en una lista
            
            for key, value in zip( columnas, values): # itera dos variables, las columnas y los valores de cada celda en la fila
                if values.index(value)== 0:
                    whereConditions.append(f" WHERE {key} = {value}")
                else:
                    if value in numeros_string or value in predeterminados:
                        comando += f"{key} = {value},"
                    else:
                        comando += f"{key} = '{value}',"

            comando = comando[:-1] # Elimina la ultima coma del String
            comando += whereConditions[-1]
            comando+=";\n" # salto de linea
            contenido +=comando
            print(comando)
            
            comando = query
        addend_arch(contenido)
        tiempo_final = datetime.now()

        print(Fore.GREEN+"\tTIEMPO DE EJECUCION")
        print("\tInicio: ",tiempo_inicio)
        print("\tFin: ",tiempo_final)
        print("\t - - - - - - -")
        print("\t",tiempo_final-tiempo_inicio,Fore.RESET)
        
    except Exception as ex:
        
        print(f" \U0000274C {red}ERROR:{freset} "+ str(ex))
        # exc_type, exc_obj, exc_tb = sys.exc_info()
        # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # print(exc_type, fname, exc_tb.tb_lineno)

# transformar datos de Excel a comandos INSERT SQL
def Excel_aInsert():
    dirFile = input('ingrese la ruta del archivo: ')
    hoja = input("Nombre de hoja: ")
    tabla = input("Nombre de tabla: ")

    #-------------
    # # Imprimir hojas del Archivo.
    # xl = pd.ExcelFile(dirFile)
    # print(xl.sheet_names)
    
    dataFrame = pd.read_excel(dirFile, sheet_name=hoja)
    
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
        values = list(dataFrame.loc[index]) # Obtiene los valores de una fila los combierte en una lista para luego ser recorrido
        for value in values: # recorre la fila
            if value in numeros_string or value in predeterminados:
                comando += f"{value},"
            else:
                comando += f"'{value}',"

        comando = comando[:-1] # Elimina la ultima coma del String
        comando+=");\n" # salto de linea
        print(comando)
        # addend_arch(comando)
        comando = query
        
    tiempo_final = datetime.now()
    print("\t",tiempo_final)

# convertir informacion de archivos de texto a sentencias INSERT SQL
def transportar_aInsert(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leer_archivo_base(ruta_archivo)
    comandoLargo = ""
    if lineaSeparada:
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split()
        comando = f"INSERT INTO {tabla}("

        tempList = lineaSeparada[0].split(",") # toma el numero de columnas para comparar con el numero de valores a ingresar e igualar las columnas
        os.system("cls")
        igualador(columnas, tempList)

        for colum in columnas:
            comando +=f"{colum.strip()}," # agrega las columnas ingresadas
        
        comando = comando[:-1] # borra la ultima coma que sobra del string, la cual genera el for anterior
        comando+=") VALUES("
        
        ini = deepcopy(comando) # copia la variable 'comando'

        print(f"{green}Tiempo de ejecucion:{freset}")
        tiempo_inicio = datetime.now()
        print("\t",tiempo_inicio)
        for item in lineaSeparada:
            elem_sep = item.split(',')
            # os.system("cls") # borra informacion de la consola o terminal
            # print(Fore.YELLOW,n,Fore.GREEN,elem_sep[0],Fore.RESET) #imprimir informacion en pantalla retrasa el proceso de transferencia de datos
            for one_item in elem_sep:
                if one_item in numeros_string or one_item in predeterminados: # valida si alguno de los campos son de tipo numero para colocarlos sin comillas
                    comando+= f" {one_item.strip()},"
                else:
                    comando+= f" '{one_item.strip()}',"
            
            comando = comando[:-1]
            comando+=");\n"
            
            comandoLargo += comando
            comando=ini        
    addend_arch(comandoLargo)
    tiempo_final = datetime.now()
    print("\t",tiempo_final)

# convertir informacion de archivos de texto a sentencias UPDATE SQL
def transportar_aUpdate(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
    os.system("cls")
    print(f'''
    |--------{red} ADVERTENCIA {freset}--------|
    La primera columna de donde se 
    toman los datos hace referencia 
    la columna condicional de WHERE
    |-----------------------------|
    ''')
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leer_archivo_base(ruta_archivo)
    comandoLargo = ""
    if lineaSeparada:
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split()
        comando = f"UPDATE {tabla} SET "

        tempList = lineaSeparada[0].split(",") # toma el numero de columnas para comparar con el numero de valores a ingresar e igualar las columnas
        os.system("cls")
        igualador(columnas, tempList)

        ini = deepcopy(comando) # copia la variable 'comando'

        print(f"{green}Tiempo de ejecucion:{freset}")
        tiempo_inicio = datetime.now()
        print("\t",tiempo_inicio)

        for item in lineaSeparada:
            elem_sep = item.split(',')
                                   
            for inx in range(len(elem_sep)):
                if elem_sep.index(elem_sep[inx])!= 0: # Evita colocar la columna condicional despues de WHERE dentro de SET
                    if elem_sep[inx] in numeros_string or elem_sep[inx] in predeterminados:
                        comando= f"{columnas[inx].strip()}={elem_sep[inx].strip()},"
                    else:
                        comando+= f"{columnas[inx].strip()}='{elem_sep[inx].strip()}',"
                else:
                    continue

            comando = comando[:-1]
            comando+=f" WHERE {columnas[0].strip()}='{elem_sep[0].strip()}';\n"
            
            comandoLargo += comando
            comando=ini        
    addend_arch(comandoLargo)
    tiempo_final = datetime.now()
    print("\t",tiempo_final)

# convertir informacion de archivos de texto a sentencias DELETE SQL
def transportar_aDelete(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
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
    lineaSeparada = leer_archivo_base(ruta_archivo)
    comandoLargo = ""
    if lineaSeparada:
        tabla = input('Tabla: ')
        columnas = input('Columna: ').split()
        columnas = columnas[0]
        comando = f"DELETE FROM {tabla} WHERE {columnas}= '"

        ini = deepcopy(comando) # copia la variable 'comando'
        os.system("cls")
        print(f"{green}Tiempo de ejecucion:{freset}")
        tiempo_inicio = datetime.now()
        print("\t",tiempo_inicio)
        
        for item in lineaSeparada:                              
            comando+= f"{item[0].strip()}';\n"
            comandoLargo += comando
            comando=ini        
    addend_arch(comandoLargo)
    tiempo_final = datetime.now()
    print("\t",tiempo_final)

#-transformar informacion de archivo de texto a sentencias INSERT SQL para la db_consulta_red_de_amor_empresarial
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

    diccionario = {
        "Documento":"",
        "Estado":"",
        "Fecha":"",
        "CreadoPor":"",
        "TipoMensaje":"",
        "Cis":"",
        "Nombre":"",
        "Telefono":"",
        "Correo":"",
        "Mensaje":""}
    
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leer_archivo_base(ruta_archivo)
    # print(lineaSeparada)
    for item in lineaSeparada:
        elem_sep = item.split(',')
        #os.system("cls") # borra informacion mostrada en la consola o terminal
        # print(Fore.YELLOW,n,Fore.GREEN,elem_sep[6],Fore.RESET)

        diccionario["tarifa"] = elem_sep[6].strip()
        diccionario["negocio"] = elem_sep[7].strip()
        diccionario["nit_empresa"] = elem_sep[0].strip()
        diccionario["tipo_de_persona"] = elem_sep[8].strip()
        diccionario["telefono_trabajador"] = elem_sep[5].strip()
        diccionario["nombre_de_la_empresa"] = elem_sep[1].strip()
        diccionario["nombre_del_trabajador"] = elem_sep[4].strip()
        diccionario["#_documento_del_trabajador"] = elem_sep[2].strip()
        diccionario["tipo_documento_del_trabajador"] = elem_sep[3].strip()
        
        queryX = 'INSERT INTO db_consulta_red_de_amor_empresarial("created_at", "created_by_id", "updated_at", "updated_by_id", "deleted", "form_id", "managementTime", "status", "currentLevel", "valuesJSON") VALUES('
        queryX += "'2020-11-10 07:30:59.394432-05'"
        queryX += ',187,'
        queryX += "'2020-11-10 07:30:59.394432-05'"
        queryX += ',187,false,3,0,'
        queryX += "'joined','gestion',"

        string = " '{"
        string +=f'"tarifa":"{diccionario["tarifa"] }",'
        string +=f'"negocio":"{diccionario["negocio"]}",'
        string +=f'"nit_empresa":{diccionario["nit_empresa"]},'
        string +=f'"tipo_de_persona":"{diccionario["tipo_de_persona"]}",'
        string +=f'"telefono_trabajador":{diccionario["telefono_trabajador"]},'
        string +=f'"nombre_de_la_empresa":"{diccionario["nombre_de_la_empresa"]}",'
        string +=f'"nombre_del_trabajador":"{diccionario["nombre_del_trabajador"]}",'
        string +=f'"#_documento_del_trabajador":{diccionario["#_documento_del_trabajador"] },'
        string +=f'"tipo_documento_del_trabajador":"{diccionario["tipo_documento_del_trabajador"]}"'
        string += "}' "
        queryX +=string + ');\n'
        addend_arch(queryX)

# - - - - Inicio de la ejecucion del programa - - - -
def inicio():
    suitch=True
    while suitch==True:
        print(f'''
        {Fore.BLACK+Back.WHITE}\U0001F41E YO TE AYUDO \U0001F41E {Back.RESET+Fore.RESET}
        [ Seleccionar una opcion ]
        [1] - INSERT\t\t[4] - transportar a JSON2 red Amor
        [2] - UPDATE\t\t[5] - Excel a Insert
        [3] - DELETE\t\t[6] -  Excel to Update
        
        [{red}*{freset}] - SALIR 
        ''')
        opt = input("R/: ")
        if opt == '1':
            transportar_aInsert()
        elif opt == '2':
            transportar_aUpdate()
        elif opt == '3':
            transportar_aDelete()
        elif opt == '4':
            transportar_aJson2_redAmor()
        elif opt == '5':
            Excel_aInsert()
        elif opt == '6':
            Excel_aUpdate()
        elif opt== '*':
            print(Fore.BLUE+"¡ADIOS!"+Fore.RESET)
            suitch=False
            quit()
        else:
            os.system("cls") # borra informacion de la consola o terminal
            print(Fore.RED,'\U0001F621 ¡OPCION INCORRECTA!',Fore.RESET)
#----------- ejecucion ------------
inicio()
