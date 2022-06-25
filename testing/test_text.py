from ..text import transport_insert
from ..main import numerosStr, predeterminados

def test_insert_output():
    '''
    target:
        prueba de conversion de datos de archivo de texto a comandos de insercion en SQL / INSERT
    state:
        development
    '''

    assert transport_insert(
        numerosStr, 
        predeterminados, 
        path_param = "../receiver/receptor.txt", 
        table_param = "people", 
        columns_param = 3) == "INSERT"
