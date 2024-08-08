from nltk.sentiment.vader import SentimentIntensityAnalyzer
from app.models import Article
from app import db


def analyze_sentiment():
    sid = SentimentIntensityAnalyzer()
    articles = Article.query.all()

    for article in articles:
        sentiment_scores = sid.polarity_scores(article.content)
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            article.sentiment = 'Positive'
        elif compound_score <= -0.05:
            article.sentiment = 'Negative'
        else:
            article.sentiment = 'Neutral'
        db.session.commit()
