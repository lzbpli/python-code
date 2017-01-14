import web

movies = [
	{
		'title':'Forrest Gump',
		'year':1994,
	},
	{
		'title': 'Titanic',
		'year':	1997,
	},
]
urls = (
'/','index'
)

class index:
	def GET(self):
		page = ''
		for m in movies:
			page += '%s(%d)\n' %(m['title'],m['year'])
		
		render = web.template.render('templates/')
		return render.index(movies)
		
	if __name__=="__main__":
		app = web.application(urls,globals())
		app.run()