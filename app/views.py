
from flask import request, redirect

from . import app
from . import db
from models import Url
from controller import encode, decode, validate_url

err_message = '''
Please make sure are sending:
A) a POST request to http://localhost:5000/shorten with form data that has a \'url\' field with your original URL or
B) a GET request to your generated shortened URL (http://localhost:5000/s/*your_code*).
'''

conflict_message = 'The shortened URL http://localhost/s/%s has already been created for %s.'


# endpoint for shortening URL
# takes form data with 'url' field that contains URL to be shortened
@app.route('/shorten', methods=['GET', 'HEAD', 'PUT', 'POST', 'DELETE'])
def shorten():

    # request should only be of POST method and should have form with url field
    if request.method != 'POST' or 'url' not in request.form:
        return err_message, 400

    true_url = request.form['url']

    # URL should start with http/s
    if not true_url.startswith('http'):
        true_url = 'http://%s' % true_url

    # if URL has already been shortened, return the shortened URL
    previous_url = Url.query.filter_by(true_url=true_url).first()
    if previous_url:
        return conflict_message % (encode(previous_url.id), true_url), 409

    # URL should be valid and return a 200
    if not validate_url(true_url):
        return '%s is an invalid URL.' % true_url, 400

    # add to db
    url = Url(true_url)
    db.session.add(url)
    db.session.commit()

    return 'The shortened URL http://localhost:5000/s/%s has been created from your original URL %s.' % (encode(url.id), true_url)


# endpoint for redirecting
# only route parameter is the base62 encoding originally produced with the URL's primary key
@app.route('/s/<path:short>', methods=['GET', 'HEAD', 'PUT', 'POST', 'DELETE'])
def reroute(short):

    # request should be of GET method
    if request.method != 'GET':
        return err_message, 400

    # decode base62 encoding to get primary key
    # for URL in DB and query DB with it
    id = decode(short)
    result = Url.query.filter_by(id=id).first()

    return redirect(result.true_url, code=302)


@app.errorhandler(404)
def page_not_found(err):
    return err_message, 404
