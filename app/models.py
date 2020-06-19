from app import db
import enum

class Ages(enum.Enum):
    kids = 'kids'
    teens = 'teens'
    adults = 'adults'
    all = 'all'

class Categories(enum.Enum):
    general = 'general'
    math = 'math'
    science = 'science'
    reading = 'reading'
    typing = 'typing'
    games = 'games'

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500))
    url = db.Column(db.String(100), unique=True)
    age = db.Column(db.Enum(Ages), default=Ages.all)
    category = db.Column(db.Enum(Categories), default=Categories.general)

    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

    def __repr__(self):
        return '<Website %r>' % self.name
