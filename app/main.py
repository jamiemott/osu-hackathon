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


def insertDB():
    # prepare a cursor object using cursor() method
    db = conn.cursor()

    # Prepare SQL query to INSERT a record into the database.
    try:
    # Execute the SQL command
        db.execute("""INSERT INTO Websites (name, description, url, age, category) VALUES (%s, %s, %s, %s, %s);""", ('Khan Academy', 'A nonprofit with the mission to provide a free, world-class education for anyone, anywhere.', 'https://www.khanacademy.org/', 'all', 'general'))
        # Commit your changes in the database
        conn.commit()
    except:
        # Rollback in case there is any error
        conn.rollback()
