# Flask Dashboard
This is a little project I've been working on to improve my Python and Flask skills.

You're free to use this code in any way you wish. Feel free to submit pull requests.

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

```python
# App config
SECRET_KEY='make-it-secure'

# Mail config
Add further instructions here

```

## Notes

### Email settings
I'm using SMTP2GO as an email service to keep things simple. You're free to use whichever service you require.
