from flask import render_template, current_app
from app.email import send_email


path = 'email/'

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    reset_timeout = int(current_app.config['RESET_TIMEOUT'])

    send_email('[Dashboard] Reset Your Password',
               sender=current_app.config['MAIL_SENDER'],
               recipients=[user.email],
               text_body=render_template(f'{path}reset_password.txt',
                                         user=user,
                                         token=token,
                                         reset_timeout=reset_timeout),
               html_body=render_template(f'{path}reset_password.html',
                                         user=user,
                                         token=token,
                                         reset_timeout=reset_timeout))
