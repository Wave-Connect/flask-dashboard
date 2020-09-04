from datetime import datetime
from flask import (render_template, flash, redirect, url_for,
    request, current_app)
from flask_login import current_user, login_required
from app import db
from app.main.forms import EditProfileForm
from app.models import User
from app.main import bp


path = 'main/'

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template(f'{path}index.html', title=('Home'))

@bp.route('/profile')
@login_required
def profile():
    return render_template(f'{path}profile.html', title=('My profile'))

@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    form = EditProfileForm(current_user.email)
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.fname = form.fname.data
        current_user.lname = form.lname.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(('Your changes have been saved.'))
        return redirect(url_for('main.profile_edit'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.fname.data = current_user.fname
        form.lname.data = current_user.lname
        form.about_me.data = current_user.about_me
    return render_template(f'{path}profile_edit.html',
                            title=('Edit Profile'),
                            form=form)
