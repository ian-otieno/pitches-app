from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm

class PitchForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    content = TextAreaField('input your pitch')
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    opinion = TextAreaField('write your comment here..')
    submit = SubmitField('submit')

class CategoryForm(FlaskForm):
    """
    Class for creating  wtf form for creating a pitch
    """
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')
