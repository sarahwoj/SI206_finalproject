from bs4 import BeautifulSoup
import requests

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


print(get_titles())

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
    print(budget_dict)
    print(len(budget_dict))


movies = get_titles()
budget = get_budget(movies)
# cur, conn = open_database('final_db.db')
# create_budget_table(cur, conn)
# add_data(budget_dict, cur, conn)



