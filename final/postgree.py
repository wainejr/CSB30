# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Instead of pip install psycopg2 try pip install psycopg2-binary
import psycopg2
import psycopg2.extras


def connect():
    try:
        conn = psycopg2.connect(
            "dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'"
        )
    except Exception as e:
        print(e)
        print("I am unable to connect to the database.")
    return conn


def send2db(table, table_name):
    conn = connect()
    cur = conn.cursor()
    for line in table:
        try:
            command = "INSERT INTO {} VALUES (".format(table_name)
            for value in line["values"]:
                if value is not None:
                    if type(value) is int:
                        command += str(value) + ","
                    else:
                        command += str("\'") + str(value) + str("\',")
                else:
                    command += "NULL,"
            if command[-1] is ",":
                command = command[:-1]
            command += ");"
            try:
                cur.execute(str(command))
                conn.commit()
            except Exception as e:
                print(e)
                print(command)
                conn.rollback()
        except Exception as e:
            print(e)
            print(command)
    cur.close()
    conn.close()