from flask import render_template, request
from app import db
from app.errors import bp


path = 'errors/'

@bp.app_errorhandler(403)
def not_found_error(error):
    return render_template(f'{path}403.html'), 403

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template(f'{path}404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template(f'{path}500.html'), 500
