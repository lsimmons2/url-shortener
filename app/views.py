
from flask import request, redirect

from . import app
from . import db
from models import Url
from controller import encode, decode



@app.route('/shorten', methods=['POST'])
def shorten():

    true_url = request.form['url']

    url = Url(true_url)
    db.session.add(url)
    db.session.commit()

    return 'The shortened URL http://localhost:5000/s/%s has been created from your original URL %s.' % (encode(url.id), true_url)


@app.route('/s/<path:short>')
def reroute(short):

    id = decode(short)
    result = Url.query.filter_by(id=id).first()

    return redirect(result.true_url, code=302)
