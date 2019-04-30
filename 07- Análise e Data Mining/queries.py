import psycopg2
import psycopg2.extras

def AVG(args, db):
	'''
		Get average of given column in given table
 		args[0]: table name
		args[1]: column name
		db: database
	'''
	print("Getting average...")
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT AVG({}) FROM {};".format(args[1], args[0]))
		return cursor.fetchall()[0][0]
	except Exception as e:
		print(e)

def STD_DEV(args, db):
	'''
		Get standard deviation of given column in given table
 		args[0]: table name
		args[1]: column name
		db: database
	'''
	print("Getting standard deviation...")
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT STDDEV({}) FROM {};".format(args[1], args[0]))
		return cursor.fetchall()[0][0]
	except Exception as e:
		print(e)

def AVG_TABLE_RATING(args, db):
	'''
		Get standard deviation of given column in given table
		At least 2 users liking
		args[0]: table name
		args[1]: column name
		args[2]: based on what column
		db: database
	'''
	print("Getting avg rating ordered...")
	conn = psycopg2.connect(db)
	cursor = conn.cursor()

	try:
		cursor.execute("SELECT {}, AVG({}) \
			FROM {} B \
			WHERE (SELECT COUNT(*) FROM {} AS C WHERE C.{} = B.{} GROUP BY {}) > 1 \
			GROUP BY {} \
			ORDER BY AVG({}) DESC;".format(
			args[1], args[2],
			args[0],
			args[0], args[1], args[1], args[1],
			args[1],
			args[2]))
		return cursor.fetchall()
	except Exception as e:
		print(e)

def POPULAR(args, db):
	'''
		Gets 10 most popular
 		args[0]: table name
		args[1]: column name
		db: database
	'''
	print("Getting most popular...")
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT {}, COUNT(*) FROM {} GROUP BY {} ORDER BY COUNT(*);".format(
			args[1], args[0], args[1]))
		return cursor.fetchall()
	except Exception as e:
		print(e)

db = "dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'"
#Q1
print(AVG(['LikesArtist', 'Rating'], db))
#Q1
print(STD_DEV(['LikesArtist', 'Rating'], db))
#Q2
print(AVG_TABLE_RATING(['LikesArtist', 'musical_artist', 'Rating'], db))
#Q3
print(POPULAR(['LikesArtist', 'musical_artist'], db))
