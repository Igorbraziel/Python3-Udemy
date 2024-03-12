import pymysql
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'costumers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']    
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


cursor.close()
connection.close()