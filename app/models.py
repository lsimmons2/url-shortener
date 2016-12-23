
from . import db
from datetime import datetime


class Url(db.Model):

    '''
    Url Model:
        - id (int): primary key
        - true_url (str): original, unadultered url
        - created (datetime): time created
    '''

    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    true_url = db.Column(db.String(255), unique=True)
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, url):
        self.true_url = url

    def __repr__(self):
        return '<Url with id %r and original url %r>' % (self.id, self.true_url)
