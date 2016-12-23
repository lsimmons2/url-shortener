
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


@app.route('/shorten', methods=['GET', 'HEAD', 'PUT', 'POST', 'DELETE'])
def shorten():

    if request.method != 'POST':
        return err_message, 400

    try:
        true_url = request.form['url']
    except:
        return err_message, 400

    if not true_url.startswith('http'):
        true_url = 'http://%s' % true_url

    previous_url = Url.query.filter_by(true_url=true_url).first()
    if previous_url:
        return conflict_message % (encode(previous_url.id), true_url), 409

    if not validate_url(true_url):
        return '%s is an invalid URL.' % true_url, 400


    url = Url(true_url)
    db.session.add(url)
    db.session.commit()

    return 'The shortened URL http://localhost:5000/s/%s has been created from your original URL %s.' % (encode(url.id), true_url)


@app.route('/s/<path:short>', methods=['GET', 'HEAD', 'PUT', 'POST', 'DELETE'])
def reroute(short):

    if request.method != 'GET':
        return err_message, 400

    id = decode(short)
    result = Url.query.filter_by(id=id).first()

    return redirect(result.true_url, code=302)


@app.errorhandler(404)
def page_not_found(err):
    return err_message, 404
