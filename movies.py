import json
import requests
import random
import pprint

api_key= "f358b1232682b075dfd6ba6b77910e56"
url = "https://api.themoviedb.org/3/movie/550?api_key=f358b1232682b075dfd6ba6b77910e56"
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"

def recommend_movies():
    print('Welcome to Movie Recommender! Select a movie you like(1-3)) or refresh the list(r).')
    i = 0
    movies = []
    while i < 3:
        movie_id = random.randrange(100,1000)
        endpoint_path = f"/movie/{movie_id}?"
        endpoint = f"{api_base_url}{endpoint_path}api_key={api_key}"
        response = requests.get(endpoint)
        try:
            print(f"[{i+1}] {response.json()['title']}")
            movies.append(int(movie_id))
            i += 1
        except KeyError:
            movie_id = random.randrange(0,1000)
            endpoint_path = f"/movie/{movie_id}?"
            endpoint = f"{api_base_url}{endpoint_path}api_key={api_key}"
            response = requests.get(endpoint)
    movie_pick = input('> ')
    if movie_pick.lower() == 'r':
        recommend_movies()
    else:
        print()
        print (f'Recommended Movies for [{movie_pick}]:')
        movie_id = int(movies[int(movie_pick)-1])
        endpoint_path = f"/movie/{movie_id}/recommendations?"
        endpoint = f"{api_base_url}{endpoint_path}api_key={api_key}"
        response = requests.get(endpoint)
        for i in range(0,3):
            print(f"[{i+1}] {response.json().get('results')[i].get('title')}")
            
recommend_movies()