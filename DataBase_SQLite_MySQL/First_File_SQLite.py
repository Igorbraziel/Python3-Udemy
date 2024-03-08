import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / 'db.sqlite3'
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (:name, :weight)'
)

cursor.execute(sql, {'name': 'Igor', 'weight': 70.5})
cursor.executemany(sql, (
    {'name': 'Nine', 'weight': 60},
    {'name': 'Isabela', 'weight': 40},
    {'name': 'Ledinha', 'weight': 55}
)
)

connection.commit()

# Closing
cursor.close() 
connection.close()