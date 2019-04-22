# Import modules
import psycopg2
import psycopg2.extras
from xml.dom import minidom
import urllib2

# teste_url = 'https://github.com/ndw/xmlss-templates/blob/master/src/dbslides.xml' 
person_url = 'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/person.xml' 
artists_url = 'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/music.xml'
movies_url = 'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/movie.xml'
conhecidos_url = 'http://dainf.ct.utfpr.edu.br/~gomesjr/BD1/data/knows.xml'

# teste_xml = minidom.parse(urllib2.urlopen(teste_url))
try:
    person_xml = minidom.parse(urllib2.urlopen(person_url))
    artists_xml = minidom.parse(urllib2.urlopen(artists_url))
    movies_xml = minidom.parse(urllib2.urlopen(movies_url))
    conhecidos_xml = minidom.parse(urllib2.urlopen(conhecidos_url))
    print(person_xml)
except Exception as e:
    print(e)



# commands = ["""CREATE TABLE IF NOT EXISTS USERS
#                       (LOGIN TEXT PRIMARY KEY NOT NULL,
#                       NAME TEXT NOT NULL,
#                       HOMETOWN TEXT NOT NULL);"""]

# # Try to connect
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