
from flask import request

from . import app
from . import db
from models import Url



@app.route('/shorten', methods=['POST'])
def shorten():

    true_url = request.form['url']

    url = Url(true_url)
    db.session.add(url)
    db.session.commit()

    return 'URL %s saved.' % url.true_url
