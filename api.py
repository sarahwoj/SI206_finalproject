from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import os

API_KEY = "44e2735d"

#returns list of 100 movie titles from 2022
def get_titles():

    list_of_movies = []

    url = 'https://www.goodhousekeeping.com/life/entertainment/g38502957/best-movies-2022/'
    r  = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    count = 0
    all = soup.find_all('span', class_="listicle-slide-hed-text")
    for title in all:
        if count < 100:
            list_of_movies.append(title.text)
            count += 1

    return list_of_movies

#returns dic of movie title and api url
def get_request_url(list):

    url_dic = {}
    for movie in list:
        if movie == 'Scream':
            title = movie.replace(' ', '+')
            base_url = f"http://www.omdbapi.com/?t={title}&y=2022&apikey={API_KEY}"
            url_dic[movie] = base_url
        elif movie == 'Bigbug':
            movie = 'Big bug'
            title = movie.replace(' ', '+')
            base_url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
            url_dic[movie] = base_url
        elif movie == "Mack and Rita":
            movie = 'Mack & Rita'
            title = movie.replace(' ', '+')
            base_url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
            url_dic[movie] = base_url
        else:
            title = movie.replace(' ', '+')
            base_url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
            url_dic[movie] = base_url
    return url_dic

#returns dic with movie title and rating
def get_ratings(dic):
    ratings_dic = {}


    for movie in dic:
        r = requests.get(dic[movie])
        result = json.loads(r.text)
        rating = result["imdbRating"]
        ratings_dic[movie] = rating

    for movie in ratings_dic:
        if ratings_dic[movie] == 'N/A':
            print(movie)

    return ratings_dic


#open database
def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#create ratings table
def create_id_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Movie_ids (movie_id INTEGER PRIMARY KEY, title TEXT)")
    conn.commit()

#add data to ratings table
def add_id_data(data, cur, conn):

    count = 1
    for movie in data:
        title = str(movie)
        id = count
        count += 1
        cur.execute("INSERT OR IGNORE INTO movie_ids (movie_id, title) VALUES (?,?)", (id, title))
    conn.commit()


#create ratings table
def create_ratings_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Ratings (movie_id INTEGER PRIMARY KEY, rating INTEGER)")
    conn.commit()

#add data to ratings table
def add_ratings_data(data, cur, conn):

   for movie in data:
        title = movie
        rating = data[movie]
        cur.execute(f'''SELECT Movie_ids.movie_id FROM Movie_ids WHERE Movie_ids.title = "{title}" ''')
        res = cur.fetchone()
        id_key = res[0]
        cur.execute("INSERT OR IGNORE INTO Ratings (movie_id, rating) VALUES (?,?)", (id_key, rating))
        conn.commit()

#running function to get titles and ratings
movies = get_titles()
urls = get_request_url(movies)
ratings_dic = get_ratings(urls)
print(ratings_dic)

#opening database and entering info
cur, conn = open_database('final_db.db')
create_ratings_table(cur, conn)
create_id_table(cur, conn)
add_id_data(ratings_dic, cur, conn)
add_ratings_data(ratings_dic, cur, conn)

#titles = movie_id, title 
#ratings = movie_id, ratings
#budget = movie_id, budget
