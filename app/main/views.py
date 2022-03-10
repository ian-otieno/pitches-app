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
    love = Pitch.query.filter_by(category = 'Love').all()
    education = Pitch.query.filter_by(category = 'Education').all()
    business = Pitch.query.filter_by(category = 'Business').all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()

    all_category = PitchCategory.get_categories()
    all_pitches = Pitch.query.order_by('id').all()
    title = "This is a golden opportunity change your life"
   
    return render_template('index.html', title=title,pitches = pitches, education = education, love = love, business = business, interview = interview, promotion = promotion, all_category=all_category, all_pitches=all_pitches)


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


@main.route('/pitches/new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description=form.description.data
        user_id = current_user._get_current_object().id
        new_pitch= Pitch(user_id =user_id,category=category,title=title, description=description)
        new_pitch.save_pitch()

        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('new.html', form = form)

@main.route('/categories/<int:id>')
def category(id):
    category = PitchCategory.query.get(id)
    if category is None:
        abort(404)

    pitches=Pitch.get_pitches(id)
    return render_template('category.html', pitches=pitches, category=category)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

  
    return render_template("profile/profile.html", user = user,pitches= pitches)

@main.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username =name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name=user.username))

    return render_template('profdile/update.html',form =form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))


@main.route('/category/love',methods= ['GET'])
def displayLoveCategory():
    love = Pitch.get_pitches('love')
    return render_template('love.html',love = love)


@main.route('/category/business',methods= ['POST','GET'])
def displayBusinessCategory():
    business = Pitch.get_pitches('business')
    return render_template('business.html',business = business)

@main.route('/category/promotion',methods= ['POST','GET'])
def displayPromotionCategory():
    promotion= Pitch.get_pitches('promotion')
    return render_template('publicity.html',promotion = promotion)

@main.route('/category/education',methods= ['POST','GET'])
def displayEducationCategory():
    educatiion = Pitch.get_pitches('education')
    return render_template('education.html',educatiion =educatiion)

@main.route('/category/interview',methods= ['POST','GET'])
def displayInterviewCategory():
    interview = Pitch.get_pitches('interview')
    return render_template('interview.html',interview = interview)



