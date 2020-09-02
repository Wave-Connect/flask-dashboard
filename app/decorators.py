from functools import wraps
from flask import abort, redirect
from flask_login import current_user



def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
