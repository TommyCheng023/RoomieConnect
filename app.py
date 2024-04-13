from flask import Flask, render_template, jsonify, flash
from config import Config
from yotpo_client import YotpoClient
from pageLogic import register_logic, login_logic
import mysql.connector
import os

# Initialization
app = Flask(__name__)
yotpo_client = YotpoClient()
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY', 'optional_default_secret_key')

db_config = {
    'host': app.config['DATABASE_HOST'],
    'user': app.config['DATABASE_USER'],
    'password': app.config['DATABASE_PASSWORD'],
    'database': app.config['DATABASE_DB']
}

db = mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_logic.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_logic.login()

@app.route('/reviews/<product_id>')
def get_product_reviews(product_id):
    try:
        reviews = yotpo_client.get_reviews(product_id)
        return jsonify(reviews)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()