from .import db
# If the user is connected or not :
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # Using ID to make sure the Data are 
    # not Conflicted when there is More than just 
    # one user with the same name:
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
