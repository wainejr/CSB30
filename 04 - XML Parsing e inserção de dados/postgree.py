import psycopg2
import psycopg2.extras

from xml2sql import getCommands

print(getCommands())

commands = ["""CREATE TABLE IF NOT EXISTS USERS
                      (LOGIN TEXT PRIMARY KEY NOT NULL,
                      NAME TEXT NOT NULL,
                      HOMETOWN TEXT NOT NULL);"""]

# Try to connect
# try:
#     conn = psycopg2.connect("dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'")

# except Exception as e:
#     print(e)
#     print("I am unable to connect to the database.")

# cur = conn.cursor()

# try:
#     for command in commands:
#         cur.execute(command)
    
# except Exception as e:
#     print(e)
#     print("I can't create table!")

# conn.commit()