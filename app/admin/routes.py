from datetime import datetime
from flask import (render_template, flash, redirect, url_for,
    request, current_app)
from flask_login import current_user, login_required
from app import db
from app.models import User
from app.admin import bp


@bp.route('/users')
@login_required
def users():
    users = User.query.all()
    page = request.args.get('page', 1, type=int)
    return render_template('admin/user_list.html', users=users)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    return render_template('admin/user.html', user=user)
