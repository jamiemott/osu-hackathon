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

@app.route('/insert' methods=['POST'])
def insertDB():
    # prepare a cursor object using cursor() method
    db = conn.cursor()

    arr = [('edX', 'Founded by Harvard and MIT, edX is home to more than 20 million learners, the majority of top-ranked universities in the world and industry-leading companies.', 'https://www.edx.org/', 'adults', 'general'), ('Coursera', 'Hundreds of free courses give you access to on-demand video lectures, homework exercises, and community discussion forums.', 'https://www.coursera.org/', 'adults', 'general'), ('Docsteach', 'National Archives online resource for teaching with primary documents.', 'https://www.docsteach.org', 'all', 'general')]
    for entry in arr:
        # Prepare SQL query to INSERT a record into the database.
        try:
            # Execute the SQL command
            db.execute("""INSERT INTO Websites (name, description, url, age, category) VALUES (%s, %s, %s, %s, %s);""", (entry)) # Commit your changes in the database
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
    db.close()
    return "Testing"
