from google.appengine.ext import ndb

class DatabaseHistory(ndb.Model):
    charityName = ndb.StringProperty()
    amountDonated = ndb.IntegerProperty()
    dateDonated = ndb.StringProperty()

class DatabaseFavs(ndb.Model):
    #TODO: insert the elements we want displayed with each favorite charity
