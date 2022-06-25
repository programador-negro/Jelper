from text import transport_insert
from main import numerosStr, predeterminados

def read_lines():
    total = set()
    with open("./response/resultado.txt") as file:
        total.add(len(file.readlines()))
    with open("./receiver/receptor.txt") as file:
        total.add(len(file.readlines()))
    return total

def test_insert():
    '''
    target:
        prueba de conversion de datos de archivo de texto a comandos de insercion en SQL / INSERT
    state:
        development
    '''

    transport_insert(
        numerosStr,
        predeterminados,
        path_param = "./receiver/receptor.txt", 
        table_param = "people", 
        columns_param = "4")
    
    read_lines()

    assert read_lines() == {3, 3}