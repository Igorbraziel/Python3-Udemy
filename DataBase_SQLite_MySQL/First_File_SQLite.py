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

cursor.execute(
    f'DELETE FROM {TABLE_NAME} WHERE id=1'
)
connection.commit()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET weight="69.50", name="New_Igor" '
    'WHERE id="3"'
)
connection.commit()

# Closing
cursor.close() 
connection.close()