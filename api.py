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

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_ratings_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Ratings (movie_id INTEGER PRIMARY KEY, title TEXT, \
        rating INTEGER)")
    conn.commit()


def add_data(data, cur, conn):

    count = 1
    for movie in data:
        title = movie
        rating = data[movie]
        id = count
        count += 1
        cur.execute("INSERT OR IGNORE INTO Ratings (movie_id, title, rating) VALUES (?,?,?)", (id, title, rating))
    conn.commit()



movies = get_titles()
urls = get_request_url(movies)
cur, conn = open_database('final_db.db')
create_ratings_table(cur, conn)
ratings_dic = get_ratings(urls)
add_data(ratings_dic, cur, conn)



#main table = movie id, title, rating, budget
#ratings table = 
