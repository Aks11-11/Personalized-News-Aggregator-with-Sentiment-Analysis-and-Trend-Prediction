import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from app.models import Article


def predict_trends():
    articles = Article.query.all()
    dates = [article.date_posted for article in articles]
    sentiments = [1 if article.sentiment == 'Positive' else -1 if article.sentiment == 'Negative' else 0 for article in
                  articles]

    df = pd.DataFrame({'date': dates, 'sentiment': sentiments})
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df.resample('D').sum().fillna(0)

    df['days'] = np.arange(len(df))
    X = df[['days']]
    y = df['sentiment']

    model = LinearRegression().fit(X, y)
    df['trend'] = model.predict(X)

    return df['trend']
