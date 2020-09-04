from datetime import datetime
from flask import (render_template, flash, redirect, url_for,
    request, current_app)
from flask_login import current_user, login_required
from app import db
from app.models import User
from app.admin import bp
from app.decorators import admin_required
from app.admin.forms import UserEditForm, UserDeleteForm, UserCreateForm


path = 'admin/'

@bp.route('/users')
@login_required
@admin_required
def user_list():
    users = User.query.all()
    page = request.args.get('page', 1, type=int)
    return render_template(f'{path}user_list.html', users=users)

@bp.route('/user/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def user_detail(id):
    user = User.query.filter_by(id=id).first_or_404()
    form = UserDeleteForm()
    if form.validate_on_submit():
        db.session.delete(user)
        db.session.commit()
        flash('User deleted.')
        return redirect(url_for('admin.user_list'))
    return render_template(f'{path}user_detail.html',
                            user=user,
                            title=(f'{user.fname} {user.lname}'),
                            form=form)


@bp.route('/user/edit/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def user_edit(id):
    user = User.query.filter_by(id=id).first_or_404()
    form = UserEditForm(user.email, render_kw ={'checked': 'True'})

    if form.validate_on_submit():
        user.email = form.email.data
        user.fname = form.fname.data
        user.lname = form.lname.data
        user.about_me = form.about_me.data
        user.admin = form.admin.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('admin.user_detail', id=user.id))
    elif request.method == 'GET':
        form.email.data = user.email
        form.fname.data = user.fname
        form.lname.data = user.lname
        form.about_me.data = user.about_me
    return render_template(f'{path}user_edit.html',
                            title=(f'{user.fname} {user.lname}'),
                            form=form,
                            user=user)


@bp.route('/user/create', methods=['GET', 'POST'])
@login_required
@admin_required
def user_create():
    form = UserCreateForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            fname=form.fname.data,
            lname=form.lname.data,
            admin=form.admin.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New user created!')
        return redirect(url_for('admin.user_detail', id=user.id))
    return render_template(f'{path}user_create.html', title='Create new user', form=form)
