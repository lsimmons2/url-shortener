<h1>URL Shortener</h1>

<h4>Starting up</h4>
<ol>
  <li>Make sure MySQL is running</li>
  <li>`pip install -r requirements.txt`</li>
  <li>`python run.py`</li>
</ol>

<h4>Using</h4>
POST to the `shorten` endpoint with you url in form data<br>
`curl -X POST -F 'url=https://facebook.com' 'http://localhost:5000/shorten'`
<br><br>
The response will be
`The shortened URL http://localhost:5000/s/2 has been created from your original URL https://facebook.com.`
<br><br>
Then navigate to `http://localhost:5000/s/2` and you will be redirected to `https://facebook.com`
