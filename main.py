import webapp2
import logging
import jinja2
import os
import database
import time

from google.appengine.api import users
from google.appengine.ext import ndb


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/search.html')
        data = {
          'user_nickname': user.nickname(),
          'logoutUrl': users.create_logout_url('/')
        }
        self.response.write(response_html.render(data))

class DetailsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        self.response.headers['Content-Type'] = 'text/html'
        response2_html = jinja_env.get_template('templates/details.html')
        ein = self.request.get('charity')
        data = {
            'ein': ein,
            'user_nickname': user.nickname(),
            'logoutUrl': users.create_logout_url('/')
        }
        self.response.write(response2_html.render(data))
        print("called")

    def post(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        name = self.request.get('name')
        website = self.request.get('website')
        deductibility = self.request.get('deductibility')
        logging.info('server saw a request to add %s, %s, and %s to list of favorites' % (name, website, deductibility))
        stored_charity = database.DatabaseFavs(name= name,
            website= website, deductibility= deductibility, username= user.nickname())
        stored_charity.put()
        ein = self.request.get('charity')
        data = {
            'ein': ein
        }
        response_html = jinja_env.get_template('templates/details.html')
        values = {
            'charities': database.DatabaseFavs.query(database.DatabaseFavs.username == user.nickname()).fetch()
        }
        self.response.write(response_html.render(data))
        print("call 2")


class DonationHistoryHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/history.html')
        # self.response.write(response_html.render())
        time.sleep(2)
        data = {
            'donations': database.DatabaseHistory.query(database.DatabaseHistory.username == user.nickname()).fetch(),
            'user_nickname': user.nickname(),
            'logoutUrl': users.create_logout_url('/')
        }
        self.response.write(response_html.render(data))

    def post(self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        charityName = self.request.get('charityName')
        amountDonated = self.request.get('amountDonated')
        dateDonated = self.request.get('dateDonated')
        logging.info('server saw a request to add %s, %s, and %s to donation history' % (charityName, amountDonated, dateDonated))
        stored_donation = database.DatabaseHistory(charityName=charityName,
            amountDonated= float(amountDonated), dateDonated=dateDonated, username= user.nickname())
        stored_donation.put()
        response_html = jinja_env.get_template('templates/history.html')
        time.sleep(2)
        data = {
            'donations': database.DatabaseHistory.query(database.DatabaseHistory.username == user.nickname()).fetch()
        }
        self.response.write(response_html.render(data))


class FavCharityHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/favorites.html')
        values = {
            "charities": database.DatabaseFavs.query(database.DatabaseFavs.username == user.nickname()).fetch(),
            'user_nickname': user.nickname(),
            'logoutUrl': users.create_logout_url('/')
        }
        self.response.write(response_html.render(values))

class DeleteDonationHistoryHandler(webapp2.RequestHandler):
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
        charity_to_delete = self.request.get('charity')
        response_html= jinja_env.get_template('templates/are_you_sure_favs.html')
        key = ndb.Key(urlsafe=charity_to_delete)
        the_charity = key.get()
        time.sleep(2)
        data = {
            "charity": the_charity.charityName,
            "charity_id": the_charity.key.urlsafe()
        }
        self.response.write(response_html.render(data))

    def post(self):
        key = ndb.Key(urlsafe=self.request.get("charity_id"))
        key.delete()

class AboutUsHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        logging.info('current user is %s' % (user.nickname()))
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/aboutus.html')
        data = {
          'user_nickname': user.nickname(),
          'logoutUrl': users.create_logout_url('/')
        }
        self.response.write(response_html.render(data))

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
    ('/delete', DeleteDonationHistoryHandler),
    ('/delete_charity', DeleteFavoriteCharityHandler)
], debug=True)
