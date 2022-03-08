from flask import render_template, redirect, url_for, abort, request
from . import main
from .. import db, photos
from ..models import User, Pitch, Comments, PitchCategory
from flask_login import login_required, current_user 
from .forms import PitchForm, CommentsForm, UpdateProfile

@main.route('/', methods= ['GET','POST'])
def index():
    '''
    view page root function that return the index page and its data
    '''
    pitches = Pitch.query.all()
    education = Pitch.query.filter_by(category = 'Education').all()
    business = Pitch.query.filter_by(category = 'Business').all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    publicity = Pitch.query.filter_by(category = 'Publicity').all()

    all_category = PitchCategory.get_categories()
    all_pitches = Pitch.query.order_by('id').all()
    title = "This is a golden chance"
   
    return render_template('index.html', title=title,pitches = pitches, education = education, business = business, interview = interview, publicity = publicity, all_category=all_category, all_pitches=all_pitches)


@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    comment_form = CommentsForm() 
    pitch=Pitch.query.get(pitch_id)
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data

        new_comment =Comments(comment=comment, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comments.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comment.html', comment_form = comment_form, comment = all_comments, pitch = pitch ) 

