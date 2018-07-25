from google.appengine.ext import ndb

class DatabaseHistory(ndb.Model):
    charityName = ndb.StringProperty()
    amountDonated = ndb.FloatProperty()
    dateDonated = ndb.StringProperty()
    username = ndb.StringProperty()

class DatabaseFavs(ndb.Model):
    name = ndb.StringProperty()
    website = ndb.StringProperty()
    deductibility = ndb.StringProperty()
    username = ndb.StringProperty()
