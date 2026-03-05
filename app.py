from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Koristimo besplatni NewsAPI (gaming vijesti)
    # Registriraj se na newsapi.org za svoj ključ, ili koristi ovaj privremeni:
    api_key = "14bdca76eebb4da3bb467f0ee0d1f3f5" # Ovdje ćeš staviti svoj pravi ključ
    url = f"https://newsapi.org/v2/everything?q=gaming&language=en&pageSize=5&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', [])
    except:
        articles = []

    return render_template('index.html', news=articles)

@app.route('/nintendo')
def nintendo():

    return render_template('nintendo.html')

if __name__ == '__main__':
    app.run(debug=True)