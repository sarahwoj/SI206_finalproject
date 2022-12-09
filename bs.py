from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import os

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

def get_budget(list):

    API_KEY = "193a95a6c0b8cbb402ad01c183d298c0"

    first_dict = {}
    id_list = []
    for x in list:
        base_url = f"https://api.themoviedb.org/3/search/movie"
        parameter = {"api_key": API_KEY, "query": x}
        r = requests.get(base_url, params=parameter)
        result = json.loads(r.text)
        d = result['results']
        first = d[0]
        id = first['id']
        id_list.append(id)

    budget_dict = {}
    for y in id_list:
        base_url_2 = f"https://api.themoviedb.org/3/movie/{y}"
        parameter = {"api_key": API_KEY}
        r2 = requests.get(base_url_2, params=parameter)
        details = json.loads(r2.text)
        title = details['title']
        budget = details['budget']
        budget_dict[title] = budget

    return budget_dict

def open_database(name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+name)
    cur = conn.cursor()
    return cur, conn

def create_budget_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Budgets (movie_id INTEGER PRIMARY KEY, budget INTEGER)")
    conn.commit()

def add_budget_data(data, cur, conn):

    count = 1
    for x in data:
        title = str(x)
        budget = data[x]
        id = count
        count += 1
        cur.execute("INSERT OR IGNORE INTO Budgets (movie_id, budget) VALUES (?,?)", (id, budget))
    conn.commit()


movies = get_titles()
budget = get_budget(movies)
print(budget)
cur, conn = open_database('final_db.db')
create_budget_table(cur, conn)
add_budget_data(budget, cur, conn)

