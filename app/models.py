from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from sqlalchemy.sql import functions

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255),index=True)
  email = db.Column(db.String(255),unique = True)
  pass_secure = db.Column(db.String(255))
  pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
  profile_pic_path = db.Column(db.String())
  comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
  upvote = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
  downvote = db.relationship('Downvote', backref = '', lazy = 'dynamic')


  def __repr__(self):
    return f'User {self.username}'

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

class Pitch(db.Model):
  '''
  '''
  __tablename__ = 'pitches'

  id = db.Column(db.Integer, primary_key = True)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  description = db.Column(db.String(), index = True)
  title = db.Column(db.String())
  category = db.Column(db.String(255), nullable=False)
  comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
  upvote = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
  downvote = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')

  @classmethod
  def get_pitches(cls, id):
    pitches = Pitch.query.order_by(pitch_id=id).desc().all()
    return pitches

  def __repr__(self):
    return f'Pitch {self.description}'

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text())
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

  def __repr__(self):
    return f'Comment: id:{self.id} comment:{self.description}'

class Upvote(db.Model):
  __tablename__='upvotes'

  id=db.Column(db.Integer,primary_key=True)
  counter=db.Column(db.Integer)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

  def save_upvotes(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def get_by_pitch(cls,pitch_id):
    upvote_by_pitch=Upvote.query.filter_by(pitch_id=pitch_id).all()
    return upvote_by_pitch

  def __repr__(self):
    return f'Upvote{self.counter}'

class Downvote(db.Model):
  __tablename__='downvotes'

  id=db.Column(db.Integer,primary_key=True)
  counter = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

  def save_downvotes(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_by_pitch(cls, pitch_id):
    downvote_by_pitch = Downvote.query.filter_by(pitch_id=pitch_id).all()
    return downvote_by_pitch

  def __repr__(self):
    return f'Downvote{self.counter}'
