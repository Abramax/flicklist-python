import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = ["Indiana Jones", "The Matrix", "The Big Lebowski", "Big", "Tootsie"]

        # TODO: randomly choose one of the movies, and return it

        return random.choice(movieList)

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        movie2 = self.getRandomMovie()

        while movie2 == movie:
            movie2 = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        content2 = "<h1>Tomorrow's Movie</h1>"
        content2 += "<p>" + movie2 + "</p>"

        self.response.write(content)
        self.response.write(content2)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
