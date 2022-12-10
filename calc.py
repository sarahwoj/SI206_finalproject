import sqlite3
import os
import csv

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def under_30(cur):

    cur.execute(f"SELECT Budgets.movie_id, Budgets.budget, Ratings.rating \
        FROM Budgets JOIN Ratings \
        ON Budgets.movie_id = Ratings.movie_id \
        WHERE Budgets.budget != 0 AND Budgets.budget < 30000000")
    result = cur.fetchall()
    print(result)

    total = 0
    for movie in result:
        rating = movie[2]
        total += rating
    
    avg = total/(len(result))

    return round(avg, 1)


def between30_70(cur):

    cur.execute(f"SELECT Budgets.movie_id, Budgets.budget, Ratings.rating \
        FROM Budgets JOIN Ratings \
        ON Budgets.movie_id = Ratings.movie_id \
        WHERE Budgets.budget != 0 AND Budgets.budget >= 30000000 AND Budgets.budget < 70000000")
    result = cur.fetchall()
    print(result)

    total = 0
    for movie in result:
        rating = movie[2]
        total += rating
    
    avg = total/(len(result))

    return round(avg, 1)

def between70_100(cur):

    cur.execute(f"SELECT Budgets.movie_id, Budgets.budget, Ratings.rating \
        FROM Budgets JOIN Ratings \
        ON Budgets.movie_id = Ratings.movie_id \
        WHERE Budgets.budget != 0 AND Budgets.budget >= 70000000 AND Budgets.budget < 100000000")
    result = cur.fetchall()
    print(result)

    total = 0
    for movie in result:
        rating = movie[2]
        total += rating
    
    avg = total/(len(result))

    return round(avg, 1)


def over_100(cur):

    cur.execute(f"SELECT Budgets.movie_id, Budgets.budget, Ratings.rating \
        FROM Budgets JOIN Ratings \
        ON Budgets.movie_id = Ratings.movie_id \
        WHERE Budgets.budget != 0 AND Budgets.budget >= 100000000")
    result = cur.fetchall()
    print(result)

    total = 0
    for movie in result:
        rating = movie[2]
        total += rating
    
    avg = total/(len(result))

    return round(avg, 1)

def create_csv(file_name):
    data_header = ["under 30", "between 30 and 70", "between 70 and 100", "over 100"]
    data = [under_30(cur), between30_70(cur), between70_100(cur), over_100(cur)]
    print(data)
    
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(data_header)
        writer.writerow(data)
        file.close()
    

cur, conn = open_database('final_db.db')
print(under_30(cur))
print(between30_70(cur))
print(between70_100(cur))
print(over_100(cur))
print(create_csv("Average Movie Rating for Different Budget Groups.csv"))



# get list of budgets without 0
# make groups from buget list (55 budgets total? how should we split them up?)
    # under 30 mil
    # between 30-70 mil
    # between 70-100 mil
    # over 100 mill
# get ratings for movies by matching movie_id
# calculate avg rating per group
# write out calculation to txt file