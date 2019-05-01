import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt


def avg(args, db):
    """
        Get average of given column in given table
        args[0]: table name
        args[1]: column name
        db: database
    """
    print("Getting average...")
    conn = psycopg2.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT AVG({}) FROM {};".format(args[1], args[0]))
        return cursor.fetchall()[0][0]
    except Exception as e:
        print(e)


def std_dev(args, db):
    """
        Get standard deviation of given column in given table
        args[0]: table name
        args[1]: column name
        db: database
    """
    print("Getting standard deviation...")
    conn = psycopg2.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT STDDEV({}) FROM {};".format(args[1], args[0]))
        return cursor.fetchall()[0][0]
    except Exception as e:
        print(e)


def avg_table_rating(args, db):
    """
        Get standard deviation of given column in given table
        At least 2 users liking
        args[0]: table name
        args[1]: column name
        args[2]: based on what column
        db: database
    """
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


def popular(args, db):
    """
        Gets 10 most popular
        args[0]: table name
        args[1]: column name
        db: database
    """
    print("Getting most popular...")
    conn = psycopg2.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT {}, COUNT(*) FROM {} GROUP BY {} ORDER BY COUNT(*);".format(
            args[1], args[0], args[1]))
        return cursor.fetchall()
    except Exception as e:
        print(e)


def conhece_normalizada(db, group=None):
    """
        Q4: Create view ConheceNormalizada
        Q6: Show the count for each user in the group
        group: group members for Q6
        db: database
    """

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


def group_user_count(args, db):
    """
        Show the count for each user in the group
        args[n]: user n to count (3 in case of exercise)
        db: database
    """

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


def movie_count_people(db):
    """
        Number of people that liked x movies
        db: database
    """
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
        n_persons = [item[0] for item in result]
        n_likes = [item[1] for item in result]

        print(n_likes)
        print(n_persons)
        xscale = []
        yscale = []
        for i in range(1, max(n_likes)+1):
            xscale.append(i)
            if i in n_likes:
                yscale.append(n_persons[n_likes.index(i)])
            else:
                yscale.append(0)

        plt.figure("Number of people that liked x movies")
        plt.xlabel("Nº of movies")
        plt.ylabel("Nº of people")
        plt.plot(xscale, yscale, 'bo')
        plt.ylim(bottom=-0.5)
        #plt.show()
    except Exception as e:
        print(e)


def people_count_movie(db):
    """
            Number of movies that are liked by x people
            db: database
        """
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
        n_likes = [item[0] for item in result]
        n_movies = [item[1] for item in result]
        print(n_likes)
        print(n_movies)
        xscale = []
        yscale = []
        for i in range(1, max(n_likes) + 1):
            xscale.append(i)
            if i in n_likes:
                yscale.append(n_movies[n_likes.index(i)])
            else:
                yscale.append(0)

        plt.figure("Number of movies with x likes")
        plt.xlabel("Nº of likes")
        plt.ylabel("Nº of movies")
        plt.plot(xscale, yscale, 'bo')
        plt.ylim(bottom=-0.5)
        # Splt.show()
    except Exception as e:
        print(e)


def friends_count_user(db):
    """
        Number of users with x friends
        db: database
    """
    print("Creating users with x friends...")
    conn = psycopg2.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT f.user_1, COUNT(*) \
                       FROM Friends F \
                       GROUP BY f.user_1")
        result = cursor.fetchall()
        persons = [item[0] for item in result]
        n_friends = [item[1] for item in result]
        print(persons)
        print(n_friends)

        xscale = [i for i in range(0, max(n_friends)+1)]
        yscale = [0]*(max(n_friends)+1)
        for i in persons:
            yscale[n_friends[persons.index(i)]] += 1

        print(xscale)
        print(yscale)
        plt.figure("Number of users with x friends")
        plt.xlabel("Nº of users")
        plt.ylabel("Nº of friends")
        plt.plot(xscale, yscale, 'bo')
        plt.ylim(bottom=-0.5)

    except Exception as e:
        print(e)


def connectivity(db):
    """
        Connectivity in the social network (as density in a graph):
        Con = Number of friendships / number of users
        db: database
    """
    print("Evaluating social network connectivity...")
    conn = psycopg2.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) \
                           FROM Friends F")
        n_friendships = (cursor.fetchall())[0][0]
        cursor.execute("SELECT COUNT(*) \
                            FROM Users U")
        n_users = (cursor.fetchall())[0][0]
        print(n_friendships)
        print(n_users)
        print("Connnectivity: " + str(n_friendships/n_users))
        return n_friendships/n_users

    except Exception as e:
        print(e)


db = "dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'"
# Q1
print(avg(['LikesArtist', 'Rating'], db))
# Q1
print(std_dev(['LikesArtist', 'Rating'], db))
# Q2
print(avg_table_rating(['LikesArtist', 'musical_artist', 'Rating'], db))
# Q3
print(popular(['LikesArtist', 'musical_artist'], db))
# Q4 to Q6
group_members = [
    "http://utfpr.edu.br/CSB30/2019/1/DI1901ianqueros",
    "http://utfpr.edu.br/CSB30/2019/1/DI1901giovanniforastieri",
    "http://utfpr.edu.br/CSB30/2019/1/DI1901wainejunior"
]
conhece_normalizada(db, group=group_members)
# Q7
movie_count_people(db)
# Q8
people_count_movie(db)
# Q9
friends_count_user(db)
connectivity(db)

plt.show()