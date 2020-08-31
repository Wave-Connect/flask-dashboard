
# Flask Dashboard
This is a little project I've (Matt) been working on to improve my Python and Flask skills. It's intended use is to demonstrate beginner-level code for beginner-level developers. You're free to use this code in any way you wish. Post a pull request with any ideas, but please keep in mind this repo is meant for beginner programmers.

## Set up

### Instructions for windows users
Assumes that you have python 3 installed.

1. Create a directory for your project
1. Create a virtual environment using `python -m venv venv`
1. 'cd' in to \venv\scripts\ and run `activate`
1. 'cd' back to the flask-dashboard folder
1. Run `pip install -r requirements.txt`

### Environment
You'll need to create a `.flaskenv` file in the flask-dashboard folder with the following:

*.flaskenv* (root)
```python
# App config
FLASK_APP=dashboard.py
FLASK_ENV=development
# Mail config
MAIL_SERVER=mail.smtp2go.com
MAIL_PORT = 587
MAIL_USE_TLS = 1
MAIL_USERNAME = 'email-username'
MAIL_PASSWORD = 'email-password'
# Below should be a list
ADMINS = ['admin1@example.com', 'admin2@example.com']
```

## Notes

### Email settings
I'm using SMTP2GO as an email service to keep things simple. You're free to use whichever service you require.

If using Gmail you'll need the settings below:

*.flaskenv (root)*
```python
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=<your-gmail-username>
MAIL_PASSWORD=<your-gmail-password>
```
Gmail requires that your account is enabled for "less secure apps". You can read more about that [here](https://support.google.com/accounts/answer/6010255?hl=en).

#### How to change the email template
More information to follow.

### Error logging
I've set up both email and file error handling. You can choose to keep as is, or remove one or all methods. See `__init__.py` under "#Log errors" and you'll see sections for both email and file error handling.

Error logs will be saved to logs/dashboard.log (new folder will be created if not already available).

The app is using noreply@MAIL_USERNAME to send error emails. You can change this manually, or add another entry to config. Look at the "# Log errors" section.

Any email addresses added to the config "ADMINS" will receive error messages. This should be in the form of a list. For example: `ADMINS = ['admin1@example.com', 'admin2@example.com']`
