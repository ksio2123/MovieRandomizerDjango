from django.shortcuts import render
from django.http.response import HttpResponse
import json, requests
from movies import Movie

# Create your views here.
URL = "https://api.themoviedb.org/3/movie/now_playing?api_key="


def home(request):

    with open("/Users/derekyu/projects/ENV/MovieRandomizerDjango/MovieRandomizerDjango/MovieRandomizer/key.json") as json_file:
        data = json.load(json_file)

    API_KEY = data["key"]
    api_url = URL + API_KEY
    movies_json = requests.get(api_url).json()

    movies = movies_json["results"]
    movie_list = []
    for movie in movies:
        picture_url = "http://image.tmdb.org/t/p/w500"
        new_movie = Movie(movie['title'],movie['release_date'], movie['overview'], picture_url+movie["poster_path"])
        movie_list.append(new_movie)
    print movie_list[0]
    return HttpResponse("hello")
