import os
import secrets
from flask import url_for, current_app
from flask_mail import Message
from flaskrental import mail

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='soorn4657@hotmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('reset_token', token=token, _external=True)}

    If you did not make this request then simply ignore this email
    '''
    mail.send(msg)