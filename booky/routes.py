import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from booky import app, db, bcrypt
from booky.forms import RegisterationForm, LoginForm, UpdateAccountForm, ArtistForm, BusinessForm, ScheduleForm, PackageForm
from booky.models import User, Client, Booking, Schedule, PaymentMethod, VenueType, Venue, EventType, Artist, PackageType, BookingStatus, Transaction, ClientLedger
from flask_login import login_user, current_user, logout_user, login_required
# from helpers import apology, login_required


# Define a route for the root URL
@app.route('/')
@app.route('/home')
def home():
    bookings = [
        {
            "month": "Dec",
            "day": "22",
            "year": "2023",
            "bride": "Hager",
            "location": "SK",
            "schedule": "9-12"
        },
        {
            "month": "Dec",
            "day": "23",
            "year": "2023",
            "bride": "Alaa",
            "location": "Ein Elhaya Resort",
            "schedule": "9-12"
        }
    ]
    return render_template("index.html", title="Ender", bookings=bookings)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterationForm()
    if request.method == "POST" and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, first_login=1)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created!, You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated and current_user.first_login:
        return redirect(url_for("new_business"))
    elif current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if current_user.first_login:
                return redirect(url_for("new_business"))
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash(f"Login UNSUCCESSFUL, Please check email and/or password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


def save_picture(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = current_user.username + "_profile" + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=["GET", "POST"])
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
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)



@app.route("/new_business", methods=['GET', 'POST'])
@login_required
def new_business():
    business_form = BusinessForm()
    artist_form = ArtistForm()
    # form = request.form
    # schedules_form = ScheduleForm()
    # packages_form = PackageForm()
    # if current_user.is_authenticated and current_user.first_login:
        
    return render_template("new_business.html", title="Business Startup", business_form=business_form, artist_form=artist_form)


@app.route("/businessname", methods=['POST'])
@login_required
def business_name():
    business_form = BusinessForm()
    if request.method == 'POST' and current_user.first_login:
        print(business_form.business_name.data)
        current_user.business_name = business_form.business_name.data
        db.session.commit()
        return "Data saved successfully!", 200


@app.route("/newartist", methods=['POST'])
@login_required
def new_artist():
    artist_form = ArtistForm()
    if request.method == 'POST' and current_user.first_login:
        artist = Artist(artist_name=artist_form.artist_name.data, artist_number=artist_form.artist_number.data, user_id=current_user.user_id)
        db.session.add(artist)
        db.session.commit()
        if request.form.get('artistCount', 0) != '':
            artist_count = 1 + int(request.form.get('artistCount', 0))
        else:
            artist_count = 1
        if artist_count > 1:
            for i in range(1, artist_count):
                artist = Artist(artist_name=request.form.get(f'artist_name_{i}'),
                                artist_number=request.form.get(f'artist_number_{i}'),
                                user_id=current_user.user_id)
                db.session.add(artist)
                db.session.commit()
        return "Data saved successfully!", 200

@app.route("/newschedule", methods=['POST'])
@login_required
def new_schedule():
    if request.method == 'POST' and current_user.first_login:
        if request.form.get('scheduleCount') != '':
            schedule_count = int(request.form.get('scheduleCount', 0))
        else:
            schedule_count = 0
        for i in range(1, schedule_count + 1):
            schedule = Schedule(schedule=request.form.get(f'schedule_{i}'), user_id=current_user.user_id)
            db.session.add(schedule)
            db.session.commit()
        return "Data saved successfully!", 200


@app.route("/newpackage", methods=['POST'])
@login_required
def new_package():
    if request.method == 'POST' and current_user.first_login:
        if request.form.get('packageCount') != '':
            package_count = int(request.form.get('packageCount', 0))
        else:
            package_count = 0
        for i in range(1, package_count + 1):
            package_type = PackageType(package_type=request.form.get(f'package_{i}'),
                                  package_type_detail=request.form.get(f'package_detail_{i}'), user_id=current_user.user_id)
            db.session.add(package_type)
            db.session.commit()
        return "Data saved successfully!", 200
        

@app.route("/neweventtype", methods=['POST'])
@login_required
def new_event_type():
    if request.method == 'POST' and current_user.first_login:
        if request.form.get('eventTypeCount') != '':
            event_type_count = int(request.form.get('eventTypeCount', 0))
        else:
            event_type_count = 0
        for i in range(1, event_type_count + 1):
            event_type = EventType(event_type=request.form.get(f'event_type_{i}'),
                                   user_id=current_user.user_id)
            db.session.add(event_type)
            db.session.commit()
        return "Data saved successfully!", 200


@app.route("/newpaymentmethod", methods=['POST'])
@login_required
def new_payment_method():
    if request.method == 'POST' and current_user.first_login:
        if request.form.get('paymentMethodCount') != '':
            payment_method_count = int(request.form.get('paymentMethodCount', 0))
            print(payment_method_count)
        else:
            payment_method_count = 0
        for i in range(1, payment_method_count + 1):
            payment_method = PaymentMethod(payment_method=request.form.get(f'payment_method_{i}'),
                                           user_id=current_user.user_id)
            db.session.add(payment_method)
            db.session.commit()
        return "Data saved successfully!", 200


