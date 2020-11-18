# Personalized Email Collection

This is a one page website, primarily featuring a form in the home page. See [design](https://www.figma.com/proto/drBkalWArE5W1hdked8sib/Peter-One-Page-Website?node-id=1%3A2&scaling=min-zoom).

The form collects user emails and site URls and stores them in a database from which a machine learning model determines how to send personalized emails based on user behaviour clicking inbox emails.

To test the application, clone this repo:

```python
$ git clone https://github.com/GitauHarrison/Peter-ML-project.git
```

Create and activate a virtual environment:

```python
$ mkvirtualenv peter_site
```

Install app dependancies:

```python
$ pip3 install -r requirements.txt
```

Run the application:

```python
$ flask run
```

### Testing the Application

Paste this URL http://127.0.0.1:5000/ on your browser's address bar to see the web application.

You can use `ngrok` to test the application on another device while the it is running on localhost. Check your terminal for something like: 

```python
* Tunnel URL:  NgrokTunnel: "http://946be86da16b.ngrok.io" -> "http://localhost:5000"
```
Paste the URL `http://946be86da16b.ngrok.io` to your mobile phone (or another device) to see the application.