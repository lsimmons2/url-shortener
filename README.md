# URL Shortener

#### Starting up
1. `git clone https://github.com/lsimmons2/url-shortener.git`
2. `cd url-shortener`
3. `pip install -r requirements.txt`
4. Make sure MySQL is running
5. `source path/to/url-shortener/setup_db.sql;` in `msql` shell (or wherever you prefer to administer MySQL)
6. `python run.py`

<h4>Using</h4>
POST to the `/shorten` endpoint with you url in form data:<br>
`curl -X POST -F 'url=https://facebook.com' http://localhost:5000/shorten`

The response will be:<br>
`The shortened URL http://localhost:5000/s/1 has been created from your original URL https://facebook.com.`

Navigate to `http://localhost:5000/s/1` and you will be redirected to `https://facebook.com`
