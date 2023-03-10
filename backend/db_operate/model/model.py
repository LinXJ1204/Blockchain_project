from backend.extension import db
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    participation = db.relationship('participation_list', backref='user', lazy='dynamic')
    paper_list = db.relationship('author', backref='user', lazy='dynamic')

class Activity(db.Model):
    __tablename__ = 'activity'
    activity_id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(70), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    participation = db.relationship('participation_list', backref='activity', lazy='dynamic')
    vote_key = db.relationship('vote_key', backref='activity', lazy='dynamic')

class participation_list(db.Model):
    __tablename__ = 'participation_list'
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey(Activity.activity_id))
    user_id = db.Column(db.Integer,db.ForeignKey(User.user_id))
    permission = db.Column(db.String(20), nullable=False)
    ballot = db.Column(db.Integer, nullable=False, unique=True)
    result = db.Column(db.String(20), nullable=True)
    key_offering = db.Column(db.Integer, nullable=True)

class paper_list(db.Model):
    __tablename__ = 'paper_list'
    paper_id = db.Column(db.Integer, primary_key=True)
    paper_title = db.Column((db.String(60)), nullable=False)
    paper_status = db.Column(db.String(20), nullable=False)
    author = db.relationship('author', backref='paper_list', lazy='dynamic')

class vote_key(db.Model):
    __tablename__ = 'vote_key'
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey(Activity.activity_id))
    key = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

class author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey(paper_list.paper_id))
    author_id = db.Column(db.Integer, db.ForeignKey(User.user_id))

