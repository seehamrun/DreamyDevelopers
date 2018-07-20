import webapp2
import logging
import jinja2
import os

from google.appengine.ext import ndb


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SearchHandler(webapp2.RequestHandler):
    #have a get and post function
class ResultsHandler(webapp2.RequestHandler):
    #have a get function
class DetailsHandler(webapp2.RequestHandler):
    #get function
class DonationHistoryHandler(webapp2.RequestHandler):
    #get function
class FavCharityHandler(webapp2.RequestHandler):
    #get function
class AboutUsHandler(webapp2.RequestHandler):
    #get function




app = webapp2.WSGIApplication([
    ('/search', SearchHandler),
    ('/results', ResultsHandler),
    ('/details', DetailsHandler),
    ('/history', DonationHistoryHandler),
    ('/favorites', FavCharityHandler),
    ('/aboutus', AboutUsHandler)
], debug=True)
