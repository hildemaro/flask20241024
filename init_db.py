import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertamos datos de ejemplo en la base de datos
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primer post', 'Contenido del primer post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Segundo post', 'Contenido del segundo post')
            )

connection.commit()
connection.close()
