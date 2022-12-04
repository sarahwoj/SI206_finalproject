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

