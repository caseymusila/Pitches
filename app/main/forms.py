from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,RadioField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

# from ..models import User


class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("Write your pitch here",validators=[Required()])
	category = RadioField('Label', choices=[ ('promotionpitch','promotionpitch'),('productpitch','productpitch')],validators=[Required()])
	submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.',validators = [Required()])
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  description = TextAreaField('Give feedback on this pitch.',validators=[Required()])
  submit = SubmitField('Comment')