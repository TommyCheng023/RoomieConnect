from flask import Flask, render_template, jsonify, session, redirect, url_for, flash
import requests
from config import Config
# from yotpo_client import YotpoClient
from pageLogic import register_logic, login_logic, roommates_logic, profile_logic, edit_logic, update_logic
import mysql.connector
import os

# Initialization
app = Flask(__name__)
# yotpo_client = YotpoClient()
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY', 'optional_default_secret_key')

# Session Auto Expiration: kick off if the user hits a 10-minute inactivity
from datetime import timedelta
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

db_config = {
    'host': app.config['DATABASE_HOST'],
    'user': app.config['DATABASE_USER'],
    'password': app.config['DATABASE_PASSWORD'],
    'database': app.config['DATABASE_DB']
}

db = mysql.connector.connect(**db_config)

@app.route('/')
def home():
    if session.get('email'):
        userName = session.get('name')
        return render_template('index.html', name=userName)
    else:
        return render_template('index.html', name=None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_logic.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_logic.login()

@app.route('/logout')
def logout():
    session.clear()
    flash('Successfully logged out!', 'info')
    return redirect(url_for('home'))

@app.route('/resources')
def resources():
    if session.get('email'):
        return render_template('resources.html')
    else:
        flash('Please sign in.', 'error')
        return redirect(url_for('login'))

@app.route('/roommates', methods=['GET'])
def roommates():
    if session.get('email'):
        return roommates_logic.showRoommates()
    else:
        flash('Please sign in.', 'error')
        return redirect(url_for('login'))
    
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if session.get('email'):
        return profile_logic.profile()
    else:
        flash('Please sign in.', 'error')
        return redirect(url_for('login'))
    
@app.route('/edit', methods=['POST'])
def edit():
    if session.get('email'):
        return edit_logic.edit()
    else:
        flash('Please sign in.', 'error')
        return redirect(url_for('login'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if session.get('email'):
        return update_logic.update()
    else:
        flash('Please sign in.', 'error')
        return redirect(url_for('login'))

@app.route('/tarot')
def tarot_card():
    if session.get('email'):
        userName = session.get('name')
        # API URL
        url = "https://tarotapi.dev/api/v1/cards/random?n=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            card = data['cards'][0] if 'cards' in data and len(data['cards']) > 0 else None
            if card:
                card_name = card.get('name')
                card_meaning_up = card.get('meaning_up')
                return render_template('tarot.html', card_name=card_name, card_meaning_up=card_meaning_up, name=userName)
            else:
                return "No card found", 404
        else:
            return "Failed to fetch tarot card", response.status_code
    else:
        flash('Please sign in to access this service.', 'error')
        return redirect(url_for('login'))
@app.route('/random-quote')
def random_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        if response.status_code == 200:
            quote = response.json()
            return render_template('quote.html', 
                                   quote_content=quote["content"], 
                                   author=quote["author"])
        else:
            return "寄", 404
    except requests.exceptions.RequestException as e:
        print(str(e))
# @app.route('/reviews/<product_id>')
# def get_product_reviews(product_id):
#     try:
#         reviews = yotpo_client.get_reviews(product_id)
#         return jsonify(reviews)
#     except Exception as e:
#         return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()