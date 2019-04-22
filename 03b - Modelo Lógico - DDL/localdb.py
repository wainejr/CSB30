import sqlite3

# conectando...
conn = sqlite3.connect('my_db.db')
# definindo um cursor
cursor = conn.cursor()

sql = open('comandos.sql').read()
comandos = sql.split(";")

for comando in comandos:
    cursor.execute(comando)
    print(comando)