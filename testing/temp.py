from colorama import init, Fore, Back # modulo que cambia el color de la fuente por consola
from datetime import datetime
import os
'''
- guardar en la dir del escritorio
- agregar opcion para guardar archivo en alguna ruta
- para INSERT
    agregar opcion para agregar los nombres de columna y la opcion para égar la dir de done se tomara el archivo con los datos

'''
init() # inicializador de colores
red, green, blue, yellow, freset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET

numeros_string = ['1','2','3','4','5', '6','7','8','9','0',
'	1	',
'	2	',
'	3	',
'	4	',
'	5	',
'	6	',
'	7	',
'	8	',
'	9	',
'	0	']
#----------------Funciones---------------------
def leer_archivo_base(ruta_archivo):
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
            return False
    except Exception as err:
        return err

def igualador(columnas1, lista2):
    len1, len2 = len(columnas1), len(lista2)
    if len1>len2:
        n = len1-len2
        for indice in range(n):
            del columnas1[indice]
    elif len1<len2:
        n = len2-len1
        for indice in range(n):
            columnas1.append('columnaX'+str(indice))
    elif len1==len2:
        print(green,"Listas de igual dimension",freset)
    else:
        pass


def addend_arch(text): # funcion para agragar strings en el archivo resultado
    file = open("./response/resultado.txt","a",encoding="utf-8")
    file.write(text+"\n") # separa por salto de linea
    file.close()

def transportar_aUpdate(): # transforma los datos a comandos UPDATE para luego ser usados en MySQL
    # UPDATE tabla SET columna=valor WHERE columna=valor
    print('''
    |-------- ADVERTENCIA --------|
    La primera columna de donde se 
    toman los datos hace referencia 
    la columna condicional de WHERE
    |-----------------------------|
    ''')
    ruta_archivo = input('Ruta del archivo: ')
    
    lineaSeparada = leer_archivo_base(ruta_archivo)

    if lineaSeparada: # valida si el archivo existe en la ruta
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split() # se introducen los nombres de columnas separados por espacio
        comando = f"UPDATE {tabla} SET "
        
        igualador(columnas, lineaSeparada)

        valores=list()
        string_valores=""
        for n, item in enumerate(lineaSeparada):
            elem_sep = item.split(',')
            os.system("cls")
            print(Fore.YELLOW,n,Fore.GREEN,elem_sep[0],Fore.RESET) # imprime en verde cada elemento que se va imprimiendo.
            
            for inx in range(len(elem_sep)):
                if elem_sep.index(elem_sep[inx])!= 0: # Evita colocar la columna condicional despues de WHERE dentro de SET
                    if elem_sep[inx] in numeros_string:
                        string_valores= f"{columnas[inx].strip()}={elem_sep[inx].strip()},"
                    else:
                        string_valores+= f"{columnas[inx].strip()}='{elem_sep[inx].strip()}',"
                else:
                    continue

            s_valores=string_valores[:-1]
            s_valores+=f" WHERE {columnas[0].strip()}='{elem_sep[0].strip()}';"
            valores.append(s_valores)
            string_valores="" # vaciado de variable
            s_valores=""      # vaciado de variable

        for valor in valores:
            addend_arch(comando+valor)

def transportar_aInsert(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leer_archivo_base(ruta_archivo)
    if lineaSeparada:
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split()
        comando = f"INSERT INTO {tabla}("
        strg=""
        for colum in columnas:
            strg +=f"{colum.strip()},"
        comando += strg[:-1]
        comando+=") VALUES("
        strg = ""
        valores = list()
        string_valores=""
        for n, item in enumerate(lineaSeparada):
            elem_sep = item.split(',')
            os.system("cls") # borra informacion de la consola o terminal
            print(Fore.YELLOW,n,Fore.GREEN,elem_sep[0],Fore.RESET)
            for one_item in elem_sep:

                if one_item in numeros_string:
                    string_valores+= f" {one_item.strip()},"
                else:
                    string_valores+= f" '{one_item.strip()}',"
            #x = len(string_valores)
            s_valores=string_valores[:-1]
            s_valores+=");"
            valores.append(s_valores)
            string_valores=""
            s_valores=""

        for valor in valores:
            addend_arch(comando+valor)

def transportar_aJson(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
    '''INSERT INTO public.db_mensaje_cis(
    id, created_at, created_by_id, updated_at, updated_by_id, deleted, deleted_at, form_id, "managementTime", status, "currentLevel", "valuesJSON")
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    diccionario = {"Documento":"","Estado":"","Fecha":"","CreadoPor":"","TipoMensaje":"","Cis":"","Nombre":"","Telefono":"","Correo":"","Mensaje":""}
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leer_archivo_base(ruta_archivo)
    for n, item in enumerate(lineaSeparada):
        elem_sep = item.split('*')
        os.system("cls") # borra informacion de la consola o terminal
        print(n," ",elem_sep)
        print(len(elem_sep))
        print(Fore.YELLOW,n,Fore.GREEN,elem_sep[0],Fore.RESET)
        diccionario["Documento"] = elem_sep[0].strip()
        diccionario["Estado"] = elem_sep[1].strip()
        diccionario["Fecha"] = elem_sep[2].strip()
        diccionario["CreadoPor"] = elem_sep[3].strip()
        diccionario["TipoMensaje"] = elem_sep[4].strip()
        diccionario["Cis"] = elem_sep[5].strip()
        diccionario["Nombre"] = elem_sep[6].strip()
        diccionario["Telefono"] = elem_sep[7].strip()
        diccionario["Correo"] = elem_sep[8].strip()
        diccionario["Mensaje"] = elem_sep[9].strip()

        string = '{'
        string += f'"cis":"{diccionario["Cis"]}",',
        string +=f'"mensaje":"{diccionario["Mensaje"]}",',
        string +=f'"tipo_mensaje":"{diccionario["TipoMensaje"]}",',
        string +=f'"id_de_llamada":',
        string +=f'"currulao_medico_cpr":"",',
        string +=f'"nombre_del_paciente":"{diccionario["Nombre"]}",',
        string +=f'"especialidades_itagui":"",',
        string +=f'"telefono_del_paciente":{diccionario["Telefono"]},',
        string +=f'"documento_del_paciente":{diccionario["Documento"]},',
        string +=f'"itagui_enfermera_p_y_p2":"",',
        string +=f'"tramite_enfermera_p_y_p":"",',
        string +=f'"correo_electronico_del_paciente":"{diccionario["Correo"]}"',
        string +='}'


        addend_arch(string)
def transportar_aJson2_redAmor(): # transforma los datos a comandos INSERT para luego ser usados en MySQL
    ''' --- Ejemplo de Query ---
    INSERT INTO db_consulta_red_de_amor_empresarial(
        "created_at", 
        "created_by_id", 
        "updated_at", 
        "updated_by_id", 
        "deleted", 
        "form_id", 
        "managementTime", 
        "status", 
        "currentLevel", 
        "valuesJSON") 
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
        '{"tarifa":"La asignada",
        "negocio":"Grandes Empleadores",
        "nit_empresa":811025289,
        "tipo_de_persona":"Población específica",
        "telefono_trabajador":3187352293,
        "nombre_de_la_empresa":"Novaventa S.A.S",
        "nombre_del_trabajador":"YESICA GIRALDO GOMEZ",
        "#_documento_del_trabajador":1036398321,
        "tipo_documento_del_trabajador":"cc"}' );'''

    diccionario = {"Documento":"","Estado":"","Fecha":"","CreadoPor":"","TipoMensaje":"","Cis":"","Nombre":"","Telefono":"","Correo":"","Mensaje":""}
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    lineaSeparada = leer_archivo_base(ruta_archivo)
    print(lineaSeparada)
    for n, item in enumerate(lineaSeparada):
        elem_sep = item.split(',')
        os.system("cls") # borra informacion de la consola o terminal
        print(Fore.YELLOW,n,Fore.GREEN,elem_sep[6],Fore.RESET)
        diccionario["tarifa"] = elem_sep[0].strip()
        diccionario["negocio"] = elem_sep[1].strip()
        diccionario["nit_empresa"] = elem_sep[2].strip()
        diccionario["tipo_de_persona"] = elem_sep[3].strip()
        diccionario["telefono_trabajador"] = elem_sep[4].strip()
        diccionario["nombre_de_la_empresa"] = elem_sep[5].strip()
        diccionario["nombre_del_trabajador"] = elem_sep[6].strip()
        diccionario["#_documento_del_trabajador"] = elem_sep[7].strip()
        diccionario["tipo_documento_del_trabajador"] = elem_sep[8].strip()
        
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
        queryX +=string + ');'
        addend_arch(queryX)

def transportar_aDelete(): # transforma los datos a comandos DELETE para luego ser usados en MySQL
    ruta_archivo = input(f'{yellow}ingrese la ruta del archivo: {freset}')
    items_sep = leer_archivo_base(ruta_archivo)
    if items_sep:
        tabla = input('Tabla: ')
        columnas = input('Columnas: ').split()
        comando = f"DELETE FROM {tabla}("
        strg=""
        for colum in columnas:
            strg +=f"`{colum.strip()}`,"
        comando += strg[:-1]
        comando+=") VALUES("
        strg = ""
        valores = list()
        string_valores=""
        for n, item in enumerate(items_sep):
            elem_sep = item.split(',')
            print(Fore.YELLOW,n,Fore.GREEN,elem_sep[0],Fore.RESET)
            for one_item in elem_sep:

                if one_item in numeros_string:
                    string_valores+= f" {one_item.strip()},"
                else:
                    string_valores+= f" '{one_item.strip()}',"
            #x = len(string_valores)
            s_valores=string_valores[:-1]
            s_valores+=");"
            valores.append(s_valores)
            string_valores=""
            s_valores=""

        for valor in valores:
            addend_arch(comando+valor)
def transportar_aSelect(): # transforma los datos a comandos SELECT para luego ser usados en MySQL
    pass

#-------- Funciones de prueba
def transportar_test():
    #for item in items_sep:
    #    elem_sep = item.split(',')
    pass

def inicio():
    suitch=True
    while suitch==True:
        print(f'''
        {Fore.YELLOW+Back.GREEN}[ Seleccionar una opcion ]{Back.RESET+Fore.RESET}
        [1] - SELECT
        [2] - INSERT
        [3] - UPDATE
        [4] - DELETE
        [5] - INSERT Red Amor Empresarial
        [{red}*{freset}] - SALIR
        ''')
        opt = input("R/: ")
        if opt == '1':
            transportar_aSelect()
        elif opt == '2':
            transportar_aInsert()
        elif opt == '3':
            transportar_aUpdate()
        elif opt == '4':
            transportar_aDelete()
        elif opt == '5':
            transportar_aJson2_redAmor()
        elif opt== '*':
            print(Fore.BLUE+"¡ADIOS!"+Fore.RESET)
            suitch=False
            quit()
        else:
            os.system("cls")
            print(Fore.RED,'¡OPCION INCORRECTA!',Fore.RESET)

#----------- ejecucion ------------
inicio()
