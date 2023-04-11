from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category="succes")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password,try again.", category="error")
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        user_name = request.form.get('userName')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist.', category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First Name must be greater than 2 characters.", category="error")
        elif len(last_name) < 2:
            flash("Last Name must be greater than 2 characters.", category="error")
        elif len(user_name) < 2:
            flash("Username must be greater than 2 characters.", category="error")
        elif password != password2:
            flash("Password don't match", category="error")
        elif len(password) < 7:
            flash("password is too short must be at lest 7 characters",
                  category="error")
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category="success")
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)
