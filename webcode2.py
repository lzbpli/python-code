import web

urls = (
'/','index'
)


db = web.database(dbn='sqlite',db='MovieSite.db')
class index:
	def GET(self):
		movies = db.select('movie')
		render = web.template.render('templates/')
		return render.index(movies)
		
if __name__=="__main__":
	app = web.application(urls,globals())
	app.run()