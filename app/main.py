import os
import psycopg2

from flask import Flask, render_template, request, redirect

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


@app.route('/contactus/')
def suggest():
    return render_template('suggest.html')


@app.route('/links/', methods=['POST', 'GET'])
def links():
    if request.method == 'POST':
        ageReq = request.form['age']  # age = request.form.get('age')
        categoryReq = request.form['category']  # category = request.form.get('category')
        
        try:
            db = conn.cursor()
            db.execute("""SELECT * FROM Websites WHERE age=%s AND category=%s;""", (ageReq, categoryReq))
            print("Resources: ")
            row = db.fetchone()

            while row is not None:
                print(row)
                row = db.fetchone()

            db.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    else:
        return render_template('links.html')


@app.route('/insert')
def insertDB():
    # prepare a cursor object using cursor() method
    db = conn.cursor()

    # arr = [('test1', 'Founded by Harvard and MIT, edX is home to more than 20 million learners, the majority of top-ranked universities in the world and industry-leading companies.', 'https://www.edx.org/', 'adults', 'general'), ('test2', 'Hundreds of free courses give you access to on-demand video lectures, homework exercises, and community discussion forums.', 'https://www.coursera.org/', 'adults', 'general')]
    arr = [('Starfall', 'On the Starfall website and in Starfall classrooms, children have fun while learning in an environment of collaboration, wonderment, and play.', 'https://www.starfall.com/h/', 'kids', 'general'),
    ('Khan Academy', 'A nonprofit with the mission to provide a free, world-class education for anyone, anywhere.', 'https://www.khanacademy.org/', 'all', 'general'),
    ('edX', 'Founded by Harvard and MIT, edX is home to more than 20 million learners, the majority of top-ranked universities in the world and industry-leading companies.', 'https://www.edx.org/', 'adults', 'general'),
    ('Coursera', 'Hundreds of free courses give you access to on-demand video lectures, homework exercises, and community discussion forums.', 'https://www.coursera.org/', 'adults', 'general'),
    ('Crash Course', 'Tons of awesome courses in one awesome channel!', 'https://www.youtube.com/user/crashcourse/featured', 'all', 'general'),
    ('Digital Public Library of America', 'Empowers people to learn, grow, and contribute to a diverse and better-functioning society by maximizing access to our shared history, culture, and knowledge.', 'https://dp.la', 'all', 'general'),
    ('National Geographic Kids', 'Explore', 'https://kids.nationalgeographic.com/', 'kids', 'science'),
    ('4-H', '4-H welcomes young people from all beliefs and backgrounds, empowering them to create positive change in their communities', 'https://4-h.org/parents/stem-agriculture/', 'kids', 'science'),
    ('Exploratorium', 'The Exploratorium is a public learning laboratory exploring the world through science, art, and human perception.', 'https://www.exploratorium.edu/', 'kids'),
    ('Science Toys', 'Make toys at home with common household materials, often in only a few minutes, that demonstrate fascinating scientific principles.', 'https://scitoys.com/', 'teens', 'science'),
    ('Bill Nye', 'Bill Nye, scientist, engineer, comedian, author, and inventor, is a man with a mission: to help foster a scientifically literate society, to help people everywhere understand and appreciate the science that makes our world work.', 'https://www.billnye.com/the-science-guy', 'kids', 'science'),
    ('Slader', 'Step by step homework solutions. Slader is an independent website supported by millions of students and contributors from all across the globe.', 'teens', 'general'),
    ('Typing', 'Extensive Keyboarding Curriculum & So Much More', 'https://www.typing.com/', 'all', 'typing'),
    ('Jungle Junior', 'Through the course of about 200 friendly, colorful videos and interactive lessons, kids will learn all about the alphabet and practice sight words, word families, and simple sentences.', 'https://www.typingclub.com/kids-typing', 'kids', 'typing'),
    ('Wolfram Alpha', 'Compute expert-level answers using Wolfram’s breakthrough algorithms, knowledge base and AI technology', 'https://www.wolframalpha.com/', 'adults', 'math'),
    ('K-5 Learning', 'Award winning program for after school and summer study. Watch your kids build reading, math and study skills online.', 'https://www.k5learning.com/', 'kids', 'math'),
    ('Purplemath', 'These free lessons are cross-referenced to help you find related material, and the "Search" box on every page is available to help you find whatever math content you''re looking for.', 'https://www.purplemath.com/', 'all', 'math'),
    ('Scholastic', 'Day-by-day projects to keep kids reading, thinking, and growing.', 'https://classroommagazines.scholastic.com/support/learnathome.html', 'kids', 'reading'),
    ('National Library Service', 'NLS is a free braille and talking book library service for people with temporary or permanent low vision, blindness, or a physical disability that prevents them from reading or holding the printed page.', 'https://www.loc.gov/nls/', 'all', 'reading'),
    ('pbskids', 'Fun games and videos.', 'https://pbskids.org/games/', 'kids', 'games'),
    ('Funbrain', 'Funbrain offers hundreds of games, books, comics, and videos that develop skills in math, reading, problem-solving and literacy.', 'https://www.funbrain.com/games', 'kids', 'games'),
    ('Mr.Nussbaum', 'Offers dozens of interactive games specifically designed to pinpoint one or several essential concepts taught in elementary years,', 'https://mrnussbaum.com/', 'kids', 'games')
    ]

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
    return "Added!"


@app.route('/delete')
def deleteDB():
    # prepare a cursor object using cursor() method
    db = conn.cursor()

    try:
        # Execute the SQL command
        db.execute("""DELETE FROM Websites;""") # Commit your changes in the database
        conn.commit()
    except:
        # Rollback in case there is any error
        conn.rollback()
    db.close()
    return "Deleted rows!"


@app.route('/select')
def get_sites():
    # prepare a cursor object using cursor() method
    db = conn.cursor()

    try:
        # Execute the SQL command
        db.execute("""SELECT * FROM Websites WHERE age='kids' AND category='general';""")
        rows = db.fetchall()
        print("The number of sites: ", db.rowcount)
        for row in rows:
            print(row)
    except:
        # Rollback in case there is any error
        conn.rollback()
    db.close()
    return "Selected rows!"