import pymysql
import pymysql.cursors
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'costumers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
    'id INT NOT NULL AUTO_INCREMENT, '
    'nome VARCHAR(50) NOT NULL, '
    'idade INT NOT NULL, '
    'PRIMARY KEY (id)'
    ')'
)
connection.commit()

cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES (%s, %s)'
)

cursor.execute(sql, ("Nine", 19))
cursor.execute(sql, ("Igor", 19))
connection.commit()

sql2 = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES '
    '(%(name)s, %(age)s)'
)

isa_dict = {
    "name": "Isabela",
    "age": 12
}

leda_dict = {
    "name": "Leda",
    "age": 43
}

cursor.executemany(sql2, (isa_dict, leda_dict))
connection.commit()
    
update = (
    f'UPDATE {TABLE_NAME} '
    'SET nome = %(name)s, idade = %(age)s '
    'WHERE id = %(id)s'
)

update_tuple = (
    {
        "name": "First change",
        "age": 77,
        "id": 2
    },
    {
        "name": "Second change",
        "age": 21,
        "id": 1
    }
)

cursor.executemany(update, update_tuple)
connection.commit()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
)

for row_dict in cursor.fetchall():
    for key, value in row_dict.items():
        print(key, ":", value)

cursor.close()
connection.close()