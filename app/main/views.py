from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment, Upvote, Downvote
from .. import db, photos   
from .forms import UpdateProfile, PitchForm, CommentsForm


@main.route('/')
def index():
    title = 'Home - Welcome to The Pitches Website'
    return render_template('index.html', title=title)


@main.route('/pitches')
def pitches():
    pitches = Pitch.query.all()
    sales = Pitch.query.filter_by(category = 'sales').all() 
    interview = Pitch.query.filter_by(category = 'interview').all()
    elevator = Pitch.query.filter_by(category = 'elevator').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()
    personal = Pitch.query.filter_by(category = 'personal').all()
    pickuplines = Pitch.query.filter_by(category = 'pickuplines').all()

    title = 'Pitches -  Welcome to The Pitches Website'
    return render_template('pitches.html', title=title , pitches = pitches, sales = sales,interview = interview, 
    elevator = elevator,promotion = promotion, personal = personal, pickuplines = pickuplines)

@main.route('/addpitches', methods = ['GET', 'POST'])
@login_required
def addpitches():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.pitches'))
        

        return(redirect(url_for('main.category')))
    title = 'Add-Pitch -  Welcome to The Pitches Website'
    return render_template('addpitch.html', title=title, pitch_form=form)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
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

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.pitches',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.pitches',id = id))



