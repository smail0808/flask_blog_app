
import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import url_for, current_app
from flaskblog import mail


def save_picture(form_picture):
    # create a random hex
    randdom_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = randdom_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/image', picture_fn)
    # resiez image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_rest_email(user):
    token = user.get_rest_token()
    msg = Message('Password Reset Request',
                  sender='smailfiki0808@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link: 
    {url_for('users.reset_password' , token =token , _external=True)} 

    If you did not make this request then simply ignor this Email and no changes made
    '''
    mail.send(msg)