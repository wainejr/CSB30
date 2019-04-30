import psycopg2
import psycopg2.extras

import xml2sql

for comando in xml2sql.getCommands():
    print(comando)