
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('app')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@localhost/urldb' % ('url_user', 'url_pass')
db = SQLAlchemy(app)

from . import views
from . import models
