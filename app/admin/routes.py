from datetime import datetime
from flask import (render_template, flash, redirect, url_for,
    request, current_app)
from flask_login import current_user, login_required
from app import db
from app.models import User
from app.admin import bp
from app.decorators import admin_required


path = 'admin/'

@bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    page = request.args.get('page', 1, type=int)
    return render_template(f'{path}user_list.html', users=users)


@bp.route('/user/<id>')
@login_required
@admin_required
def user(username):
    user = User.query.filter_by(id=id).first_or_404()
    page = request.args.get('page', 1, type=int)
    return render_template(f'{path}user.html', user=user)
