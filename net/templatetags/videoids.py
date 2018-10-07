from django import template
import requests
register=template.Library()

@register.filter(name='datas')
def data(value):
	response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q={value}%2DMovie%2DOfficial+&type=video&videoCaption=closedCaption&key=AIzaSyCUJSh3QGecsOPq-orMsEiLn5muL1sotKQ')	
	datas = response.json()
	print(datas.keys())
	try:
		iddatas = datas['items'][0]['id']['videoId']
	except:
		return 'sdddfdssxxx'	
	print(iddatas)
	return iddatas

@register.filter(name='genreids')
def getter(a):
	return {28:"Action",12:"Adventure",16:"Adventure",35:"Comedy",80:"Crime",99:"Documentary",18:"Drama",10751:"Family",14:"Fantasy",36:"History",27:"Horror",10402:"Music", 9648: "Mystery",878:"Science Fiction",10770: "TV Movie", 53: "Thriller",10752: "War",37: "Western"}.get(a)