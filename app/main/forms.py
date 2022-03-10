from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    title = StringField("Your Nickname", validators=[Required()])
    description = TextAreaField("Wrie your pitch..", validators=[Required()])
    category = SelectField("Category", choices=[('Education','Education'),('Business','Business'),('Interview', 'Interview'),('Publicity', 'Publicity')], validators=[Required()])
    submit = SubmitField("Submit Pitch")

class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave your comment', validators=[Required()])
    submit = SubmitField("Comments")

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourslef.", validators=[Required()])  
    submit = SubmitField('Submit')

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class DownvoteForm(FlaskForm):
	submit = SubmitField()