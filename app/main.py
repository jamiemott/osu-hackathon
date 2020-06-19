import os
import psycopg2

from flask import Flask, render_template

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about/')
def about():
   return render_template('about.html')

@app.route('/books/')
def books():
   return render_template('books.html')

@app.route('/links/')
def links():
   return render_template('links.html')
