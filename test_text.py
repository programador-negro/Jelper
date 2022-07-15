from text import transport_insert
from main import numerosStr, predeterminados

def read_lines(validate_insert_param = False):
    total = list()
    if validate_insert_param:
        with open("./response/resultado.txt") as file:
            lines: list = file.readlines()
            suma, result = len(lines), 0
            for x in lines:
                if x[0:6] == 'INSERT' or x[0:6] == 'insert':
                    result += 1
        if suma == result: return True
        else: return False
    else:
        with open("./response/resultado.txt") as file:
            total.add(len(file.readlines()))
        with open("./receiver/receptor.txt") as file:
            total.add(len(file.readlines()))
        return total

def test_insert():
    '''
    target:
        prueba de conversion de datos de archivo de texto a comandos de inserción en SQL / INSERT
    state:
        finished
    '''

    transport_insert(numerosStr, predeterminados, path_param = "./receiver/receptor.txt", table_param = "people", columns_param = "4")

    assert read_lines()[0] == read_lines()[1]

def test_start_with_insert():
    '''
    target:
        prueba que cada linea del archivo inicie con la palabra INSERT
    state:
        finished
    '''

    transport_insert(numerosStr, predeterminados, path_param = "./receiver/receptor.txt", table_param = "people", columns_param = "4")
    assert read_lines(validate_insert_param = True) == True