from flask import render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Article
from app import db
from app.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.news_fetcher import fetch_news
from app.sentiment_analysis import analyze_sentiment
from app.trend_prediction import predict_trends


@main.route('/dashboard')
@login_required
def dashboard():
    fetch_news(current_user.news_preferences or "technology")
    analyze_sentiment()
    articles = Article.query.filter_by(user_id=current_user.id).all()
    trend = predict_trends().tolist()

    return render_template('dashboard.html', articles=articles, trend=trend)
