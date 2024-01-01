import os
from PIL import Image
from flask_login import current_user
from flask import current_app

def save_picture(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = current_user.username + "_profile" + f_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
