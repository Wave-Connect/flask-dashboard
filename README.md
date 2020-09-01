


# Flask Dashboard
This is a little project I (Matt) have been working on to improve my Python and Flask skills. It's intended use is to demonstrate beginner-level code. You're free to use this code in any way you wish (a star or comment would be nice). Suggestion? Post a pull request with any ideas, but please keep in mind this repo is meant for beginner programmers.

## Set up

### Windows users
**I don't use mac, sorry :/**
I'm going to assume that you already have have python 3 installed.

1. `mkdir` - Create a directory for your project
2. `cd` into the new folder. Once there, run;
3. `python -m venv venv` to create a virtual environment. Next,
4. `cd` into the *\venv\scripts\* folder and run;
5. `activate` to start the virtual environment. After the venv activates,
6. `cd..` back to the flask-dashboard folder. Finally, run
7. `pip install -r requirements.txt`

### Environment
You'll need to create a `.flaskenv` file in the flask-dashboard folder with the following:

###### */flask-dashboard/.flaskenv*
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
LOG_TO_STDOUT = 0
# Below should be a list
ADMINS = ['admin1@example.com', 'admin2@example.com']
```

### Create the database
###### Terminal > */flask-dashboard*
```shell
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Run the app!
###### Terminal > */flask-dashboard*
```shell
flask run
```

## Testing
###### Terminal > */flask-dashboard*
```shell
python tests.py
```
Go to root (`flask-dashboard`) and run python tests.py

## Notes

### Email settings
I'm using SMTP2GO as an email service to keep things simple. You're free to use whichever service you require.

Here are some example set-ups.

##### SMTP2GO
###### */flask-dashboard/.flaskenv*
```html
MAIL_SERVER = mail.smtp2go.com
MAIL_PORT = 587
MAIL_USE_TLS = 1
MAIL_USERNAME = 'enter-username'
MAIL_PASSWORD = 'enter-password'
MAIL_SENDER = 'noreply@your-domain.com'
```
##### Gmail
###### */flask-dashboard/.flaskenv*
```shell
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=<your-gmail-username>
MAIL_PASSWORD=<your-gmail-password>
MAIL_SENDER=<email-of-sender>
```
Gmail requires that your account is enabled for "less secure apps". You can read more about that [here](https://support.google.com/accounts/answer/6010255?hl=en).

#### Reset timeouts
You can change the reset timeout by amending the 'RESET_TIMEOUT' int value in `config.py` or your `.flaskenv` file. If you're planning on passing this through to a jina template, you'll need to wrap in an int. For example:
```python
int(app.config['RESET_TIMEOUT'])
```
#### How to change the email template
Simply change the .txt and .html templates inside the *templates/email* folder.

### Error logging
I've set up both email and file error handling. You can choose to keep as is, or remove one or all methods. See `__init__.py` under "#Log errors" and you'll see sections for both email and file error handling.

Error logs will be saved to logs/dashboard.log (new folder will be created if not already available).

The app is using MAIL_SENDER to send error emails. Simply change this in `config.py` or `.flaskenv`.

Any email addresses added to the config "ADMINS" will receive error messages. This should be in the form of a list. For example: `ADMINS = ['admin1@example.com', 'admin2@example.com']`

### Displaying dates and times
There are a few ways to display dates and times with jinja templates thanks to the flask-moment library.

To display a date and time such as **August 31, 2020 7:01 PM** use:
```html
<!-- Format -->
{{ moment(dateofthing).format('LLL') }}
<!-- Example -->
{{ moment(user.last_seen).format('LLL') }}
```
To display a more human readable text such as **A few minutes ago** use:
```html
<!-- Format -->
{{ moment(dateofthing) }}
<!-- Example -->
{{ moment(user.last_seen) }}
```
## Credits
Much of the code I've used in the dashboard app comes from the [Flask Mega-Tutorial]([https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)), created by the talented [Miguel Grinberg](https://blog.miguelgrinberg.com/post/about-me).
