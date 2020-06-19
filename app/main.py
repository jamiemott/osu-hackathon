import os
import psycopg2

from flask import Flask, render_template
app = Flask(__name__)

DATABASE_URL = os.environ['postgres://uxljrqiaodhmkp:26a74ef19a7168996b17cfd2fdfb63fd07eb685db6b13320b9ea943a77dae747@ec2-34-224-229-81.compute-1.amazonaws.com:5432/d34ui9hdrc2rdh']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


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
