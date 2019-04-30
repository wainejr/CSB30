import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt

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

def CONHECE_NORMALIZADA(db, group = None):
	'''
		Q4: Create view ConheceNormalizada
		Q6: Show the count for each user in the group
		group: group members for Q6
		db: database
	'''
	
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		print("Creating view...")
		cursor.execute("CREATE VIEW ConheceNormalizada  AS \
			SELECT user_1 AS user1, user_2 AS user2\
			FROM Friends UNION \
			SELECT user_2 AS user1, user_1 AS user2\
			FROM Friends;")
		cursor.execute("SELECT * FROM ConheceNormalizada;")
		print(cursor.fetchall())
		print("Getting user count...")
		cursor.execute("SELECT user1, COUNT(*)  \
			FROM ConheceNormalizada \
			WHERE user1 IN (\'{}\', \'{}\', \'{}\') \
			GROUP BY user1;".format(group[0], group[1], group[2]))
		print(cursor.fetchall())
		# return cursor.fetchall()
	except Exception as e:
		print(e)

def GROUP_USER_COUNT(args, db):
	'''
		Show the count for each user in the group
 		args[n]: user n to count (3 in case of exercise)
		db: database
	'''
	
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT user1, COUNT(*)  \
			FROM ConheceNormalizada \
			WHERE user1 IN (\"{}\", \"{}\", \"{}\") \
			GROUP BY user1;".format(args[0], args[1], args[2]))
		return cursor.fetchall()
	except Exception as e:
		print(e)

def MOVIE_COUNT_PEOPLE(db):
	'''
		Number of people that liked x movies
		db: database
	'''
	print("Creating people that liked x movies graph...")
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		
		# cursor.execute("SELECT * FROM likesmovie")
		cursor.execute("SELECT mc.movie_count, COUNT(*) \
			FROM (SELECT user_likes, COUNT(*) AS movie_count FROM likesmovie GROUP BY user_likes) AS mc \
			GROUP BY mc.movie_count \
			ORDER BY mc.movie_count;")
		result = cursor.fetchall()
		xscale = [item[0] for item in result]
		yscale = [item[1] for item in result]
		print(xscale, yscale)
		plt.figure("people by x movies")
		plt.plot(xscale, yscale)
		# plt.show()
	except Exception as e:
		print(e)

def PEOPLE_COUNT_MOVIE(db):
	'''
		Number of movies that are liked by x people
		db: database
	'''
	print("Creating movies liked by x people...")
	conn = psycopg2.connect(db)
	cursor = conn.cursor()
	try:
		
		# cursor.execute("SELECT * FROM likesmovie")
		cursor.execute("SELECT mc.user_count, COUNT(*) \
			FROM (SELECT movie_id, COUNT(*) AS user_count FROM likesmovie GROUP BY movie_id) AS mc \
			GROUP BY mc.user_count \
			ORDER BY mc.user_count;")
		result = cursor.fetchall()
		xscale = [item[0] for item in result]
		yscale = [item[1] for item in result]
		print(xscale, yscale)
		plt.figure("Movies by x people")
		plt.plot(xscale, yscale)
		plt.show()
	except Exception as e:
		print(e)

db = "dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'"
#Q1
# print(AVG(['LikesArtist', 'Rating'], db))
#Q1
# print(STD_DEV(['LikesArtist', 'Rating'], db))
#Q2
# print(AVG_TABLE_RATING(['LikesArtist', 'musical_artist', 'Rating'], db))
#Q3
# print(POPULAR(['LikesArtist', 'musical_artist'], db))
#Q4 to Q6
group_members = [
	"http://utfpr.edu.br/CSB30/2019/1/DI1901ianqueros",
	"http://utfpr.edu.br/CSB30/2019/1/DI1901giovanniforastieri",
	"http://utfpr.edu.br/CSB30/2019/1/DI1901wainejunior"
]
# CONHECE_NORMALIZADA(db, group=group_members)
#Q7
MOVIE_COUNT_PEOPLE(db)
#Q8
PEOPLE_COUNT_MOVIE(db)