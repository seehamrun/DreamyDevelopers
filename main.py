import webapp2
import logging
import jinja2
import os
#import database

from google.appengine.api import users
from google.appengine.ext import ndb


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/index.html')
        self.response.write(response_html.render())
# class SearchHandler(webapp2.RequestHandler):
#     #have a get and post function
# class ResultsHandler(webapp2.RequestHandler):
#     #have a get function
# class DetailsHandler(webapp2.RequestHandler):
#     #get function
# class DonationHistoryHandler(webapp2.RequestHandler):
#     #get function
# class FavCharityHandler(webapp2.RequestHandler):
#     #get function
class AboutUsHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response2_html = jinja_env.get_template('templates/aboutus.html')
        self.response.write(response2_html.render())

class SearchHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response3_html = jinja_env.get_template('templates/search.html')
        self.response.write(response3_html.render())

class ResultsHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response3_html = jinja_env.get_template('templates/results.html')
        self.response.write(response3_html.render())


app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler),
    ('/results', ResultsHandler),
    # ('/details', DetailsHandler),
    # ('/history', DonationHistoryHandler),
    # ('/favorites', FavCharityHandler),
    ('/aboutus', AboutUsHandler)
], debug=True)
