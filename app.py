from flask import Flask, jsonify, redirect, render_template, request, url_for
from models import Smoothies, db
from utils import initialize_db


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    initialize_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/smoothies')
def smoothies():
    print('smoothies called')
    all_smoothies_list = Smoothies.query.all()
    print(all_smoothies_list)
    return render_template('smoothies.html', smoothies_list = all_smoothies_list)


if __name__ == '__main__':
    app.run(debug=True, port=8080)

