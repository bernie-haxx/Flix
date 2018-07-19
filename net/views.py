from django.shortcuts import render
import requests



# Create your views here.


def index(request):
	popular = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=c2ebfc2b45b369bc6c954edff69fad57')
	populardata = popular.json()
	datapopular = populardata['results']
	upcoming = requests.get('https://api.themoviedb.org/3/movie/upcoming?api_key=c2ebfc2b45b369bc6c954edff69fad57')
	upcomingdata = upcoming.json()
	dataupcoming = upcomingdata['results']
	nowplaying = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=c2ebfc2b45b369bc6c954edff69fad57')
	nowplayingdata = nowplaying.json()
	datanowplaying = nowplayingdata['results']

	return render(request,'index.html',{
		'popular' : datapopular,
		'upcoming':dataupcoming,
		'now_playing':datanowplaying
	})
