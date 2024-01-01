from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from booky import db, bcrypt
from booky.models import User
from booky.users.forms import RegisterationForm, LoginForm, UpdateAccountForm
from booky.users.utils import save_picture


users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegisterationForm()
    if request.method == "POST" and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, first_login=1)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created!, You are now able to log in", "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="register", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated and current_user.first_login:
        return redirect(url_for("business_add.new_business"))
    elif current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if current_user.first_login:
                return redirect(url_for("business_add.new_business"))
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash(f"Login UNSUCCESSFUL, Please check email and/or password", "danger")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("users.account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)


