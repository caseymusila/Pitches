from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import PitchForm,UpdateProfile,CommentForm
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .. import db,photos

@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  title = 'Pitch'

  return render_template('index.html',title = title)


@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()
  # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
  if form.validate_on_submit():
    description = form.description.data
    title = form.title.data
    owner_id = current_user
    category = form.category.data
    print(current_user._get_current_object().id)
    new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
    db.session.add(new_pitch)
    db.session.commit()
        
        
    return redirect(url_for('main.pitch_disp'))
  return render_template('pitches.html',form=form)

@main.route('/pitches/', methods = ['GET','POST'])
@login_required
def pitch_disp():
  title = 'Pitches Display'
  pitch = Pitch.query.filter_by().first()
  interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
  promotionpitch = Pitch.query.filter_by(category = "promotionpitch")
  productpitch = Pitch.query.filter_by(category = "productpitch")

  return render_template('pitches_disp.html', title = title, pitch = pitch, interviewpitch = interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
  form = CommentForm()
  pitch=Pitch.query.get(pitch_id)
  if form.validate_on_submit():
    description = form.description.data

    new_comment = Comment( description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
    db.session.add(new_comment)
    db.session.commit()


    return redirect(url_for('.new_comment', pitch_id= pitch_id))

  all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
  return render_template('comment.html', form = form, comment = all_comments, pitch = pitch )

@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_by_pitch(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch_disp', id=id))
        else:
            continue
    new_vote = Upvote(user_id=current_user._get_current_object().id, pitch_id=id)
    new_vote.save_upvotes()
    return redirect(url_for('main.index', id=id))

@main.route('/dislike/<int:id>', methods=['POST', 'GET'])
@login_required
def dislike(id):
    get_pitch = Downvote.get_by_pitch(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitch:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch_disp', id=id))
        else:
            continue
    new_downvote = Downvote(user_id=current_user._get_current_object().id, pitch_id=id)
    new_downvote.save_downvotes()
    return redirect(url_for('main.pitch_disp', id=id))

@main.route('/user/<uname>')
@login_required
def profile(uname):
  # categories = Category.query.all()
  user = User.query.filter_by(username = uname).first()
  title = current_user.username + " | Pitch"
  if user is None:
    abort(404)
  # pitches = Pitch.get_user_pitch(user.id)
  return render_template("profile/profile.html", user = user, title=title)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  # categories = Category.query.all()
  if user is None:
    abort(404)
    
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data
  
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  return redirect(url_for('main.profile',uname=uname))