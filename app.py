import os
from dotenv import load_dotenv

from flask import Flask, render_template
import requests
load_dotenv()                               # Učitava .env file

app = Flask(__name__)

@app.route('/')
def index():
    # Koristimo besplatni NewsAPI (gaming vijesti)
    # Registriraj se na newsapi.org za svoj ključ, ili koristi ovaj privremeni:
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=gaming&language=en&pageSize=5&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', [])
    except:
        articles = []

    return render_template('index.html', news=articles)

@app.route('/konzole')
def konzole():
    return render_template('konzole.html')

@app.route("/pc")
def pc():
    return render_template("pc.html")

@app.route("/boardgames")
def boardgames():
    return render_template("boardgames.html")

@app.route("/bg_news")
def bg_news():
    return render_template("bg_news.html")

@app.route("/bg_reviews")
def bg_reviews():
    return render_template("bg_reviews.html")

@app.route("/bg_top")
def bg_top():
    return render_template("bg_top.html")

@app.route("/mobile")
def mobile():
    return render_template("mobile.html")





if __name__ == '__main__':
    app.run(debug=True)