from flask import Flask, jsonify, redirect, render_template, request, url_for
from models import Smoothies, db
from utils import initialize_db


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.create_all()
    initialize_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/smoothies')
def smoothies():
    all_smoothies_list = Smoothies.query.all()

    return render_template('smoothies.html', smoothies_list = all_smoothies_list)
