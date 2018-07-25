import webapp2
import logging
import jinja2
import os
import database
import time
# import database

from google.appengine.api import users
from google.appengine.ext import ndb


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/search.html')
        self.response.write(response_html.render())

class DetailsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response2_html = jinja_env.get_template('templates/details.html')
        ein = self.request.get('charity')
        data = {
            'ein': ein
        }
        self.response.write(response2_html.render(data))

class DonationHistoryHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/history.html')
        # self.response.write(response_html.render())
        time.sleep(2)
        data = {
            'donations': database.DatabaseHistory.query().fetch()
        }
        self.response.write(response_html.render(data))

    def post(self):
        charityName = self.request.get('charityName')
        amountDonated = self.request.get('amountDonated')
        dateDonated = self.request.get('dateDonated')
        stored_donation = database.DatabaseHistory(charityName=charityName,
            amountDonated= float(amountDonated), dateDonated=dateDonated)
        stored_donation.put()
        response_html = jinja_env.get_template('templates/history.html')
        time.sleep(2)
        data = {
            'donations': database.DatabaseHistory.query().fetch()
        }
        self.response.write(response_html.render(data))


class FavCharityHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/favorites.html')
        values = {
            "charities": database.DatabaseFavs.query().fetch()
        }
        self.response.write(response_html.render(values))

    def post(self):
        name = self.request.get('charityN')
        website = self.request.get('charityWebsite')
        deductibility = self.request.get('charityDeduct')
        stored_charity = database.DatabaseFavs(name= name,
            website= website, deductibility= deductibility)
        stored_charity.put()
        response_html = jinja_env.get_template('templates/favorites.html')
        values = {
            'charities': database.DatabaseFavs.query().fetch()
        }
        self.response.write(response_html.render(data))

class DeleteCharityHandler(webapp2.RequestHandler):
    def get(self):
        charity_to_delete = self.request.get('charity_id')
        response_html= jinja_env.get_template('templates/you_sure.html')
        key = ndb.Key(urlsafe=charity_to_delete)
        the_charity = key.get()
        data = {
            "charityName": the_charity.charityName,
            "charity_id": the_charity.key.urlsafe()
        }
        self.response.write(response_html.render(data))
    def post(self):
        key = ndb.Key(urlsafe=self.request.get('charity_id'))
        key.delete()

class DeleteFavoriteCharityHandler(webapp2.RequestHandler):
    def get(self):
        charity_to_delete = self.request.get('charity_id')
        response_html= jinja_env.get_template('templates/favorites.html')
        key = ndb.Key(urlsafe=charity_to_delete)
        the_charity = key.get()
        time.sleep(2)
        data = {
            "charityName": the_charity.charityName,
            "charity_id": the_charity.key.urlsafe()
        }
        self.response.write(response_html.render(data))
    def post(self):
        key = ndb.Key(urlsafe=self.request.get('charity_id'))
        time.sleep(2)
        key.delete()

class AboutUsHandler(webapp2.RequestHandler):
    def get (self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/aboutus.html')
        self.response.write(response_html.render())

# class SearchHandler(webapp2.RequestHandler):
#     def get (self):
#         self.response.headers['Content-Type'] = 'text/html'
#         response_html7 = jinja_env.get_template('templates/search.html')
#         self.response.write(response_html7.render())

# class ResultsHandler(webapp2.RequestHandler):
#     def get (self):
#         self.response.headers['Content-Type'] = 'text/html'
#         response8_html = jinja_env.get_template('templates/results.html')
#         self.response.write(response8_html.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    # ('/search', SearchHandler),
    # ('/results', ResultsHandler),
    ('/details', DetailsHandler),
    ('/history', DonationHistoryHandler),
    ('/favorites', FavCharityHandler),
    ('/aboutus', AboutUsHandler),
    ('/delete', DeleteCharityHandler)
], debug=True)
