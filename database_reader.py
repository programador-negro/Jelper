import pymysql.cursors as pycursors
from config.settings import DATABASES


connection = pymysql.connect(
    host=DATABASES['default']['host'],
    user=DATABASES['default']['user'],
    database=DATABASES['default']['name'],
    cursorclass=pycursors.DictCursor
)


def get_info_from_database(table: str):
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM {table};"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
