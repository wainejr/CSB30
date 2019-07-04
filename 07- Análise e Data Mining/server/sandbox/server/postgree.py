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


def fetch_from_query(query_cmd):
    try:
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute(query_cmd)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
            return []
    except Exception as e:
        print(e)
        return []
