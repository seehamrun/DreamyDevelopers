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

class DetailsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response2_html = jinja_env.get_template('templates/details.html')
        self.response.write(response2_html.render())

class DonationHistoryHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response3_html = jinja_env.get_template('templates/history.html')
        self.response.write(response3_html.render())

class FavCharityHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response4_html = jinja_env.get_template('templates/favorites.html')
        self.response.write(response4_html.render())

class AboutUsHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response5_html = jinja_env.get_template('templates/aboutus.html')
        self.response.write(response5_html.render())

class SearchHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response6_html = jinja_env.get_template('templates/search.html')
        self.response.write(response6_html.render())

# class ResultsHandler(webapp2.RequestHandler):
#     def get (self):
#         self.response.headers['Content-Type'] = 'text/html'
#         response7_html = jinja_env.get_template('templates/results.html')
#         self.response.write(response7_html.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
<<<<<<< HEAD
    #('/search', SearchHandler),
    # ('/results', ResultsHandler),
=======
    ('/search', SearchHandler),
    ('/results', ResultsHandler),
>>>>>>> 21fa4c6ed6e1e5feea857c0a7d926eadf3bbffab
    ('/details', DetailsHandler),
    ('/history', DonationHistoryHandler),
    ('/favorites', FavCharityHandler),
    ('/aboutus', AboutUsHandler)
], debug=True)
