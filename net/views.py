from django.shortcuts import render
import requests



# Create your views here.


def index(request):
	popular = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=c2ebfc2b45b369bc6c954edff69fad57')
	populardata = popular.json()
	datapopular = populardata['results']
