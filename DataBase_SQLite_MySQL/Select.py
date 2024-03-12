import sqlite3
from First_File_SQLite import TABLE_NAME, DB_PATH

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)
connection.commit()

if __name__ == '__main__':
    for row in cursor.fetchall():
        id_, name, weight = row
        print(id_, name, weight)

# Closing
cursor.close() 
connection.close()