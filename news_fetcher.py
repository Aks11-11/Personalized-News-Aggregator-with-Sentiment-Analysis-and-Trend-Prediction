import requests
from app.models import Article
from app import db

API_KEY = 'YOUR_NEWS_API_KEY'

def fetch_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    news_data = response.json()

    for article in news_data['articles']:
        new_article = Article(
            title=article['title'],
            content=article['description'],
            sentiment='Neutral',  # Placeholder, actual sentiment will be set later
            user_id=1  # Placeholder, use actual user id in production
        )
        db.session.add(new_article)
    db.session.commit()
