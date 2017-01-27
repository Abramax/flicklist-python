import webapp2
import cgi


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
def getCurrentWatchList():
    """Returns user's current watchlist"""
    return["Harry Potter!", "Harry and The Hendersons", "Dirty Harry", "Dirty Harry 2"]

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """
        #Create the <options for our cross off <select>
        crossoff_options = ""
        for movie in getCurrentWatchList():
                crossoff_options += "<option value='{0}'>{0}</option>".format(movie)

        cross_form = """
        <form action="/cross" method="post">
            <label>
                I want to cross off
                <select name="cross_off_movie">
                    {0}
                </select>
                from my watchlist.
            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
        """.format(crossoff_options)

        #If we have an error show it on the page
        error = self.requiest.get("error")
        if error:
            error_element = "<p class = 'error'>" + cgi.escapte(error, quote=True) + "</p>"
        else:
            error_element = ""

        main_content = edit_header + add_form + cross_form + error_element
        content = page_header + edit_header + add_form + cross_form + page_footer
        self.response.write(content)

class CrossOffMovie(webapp2.RequestHandler):
    def post(self):

        crossoff_movie = self.request.get("cross_off_movie")


        cross_off_element = "<strike>" + crossoff_movie + "</strike>"
        sentence = cross_off_element + " has been crossed off your Watchlist."

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross', CrossOffMovie)
], debug=True)
