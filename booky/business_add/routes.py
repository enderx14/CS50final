from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required
from booky import db
from booky.models import Schedule, PaymentMethod, VenueType, EventType, Artist, PackageType, BookingStatus
from booky.business_add.forms import ArtistForm, PackageForm, BusinessForm, ArtistMainForm


business_add = Blueprint("business_add", __name__)

@business_add.route("/new_business", methods=["GET", "POST"])
@login_required
def new_business():
    business_form = BusinessForm()
    artist_form = ArtistForm()
    artist_main_form = ArtistMainForm()
    if request.method == "POST":
        data = request.json
        if data and data.get("done"):
            current_user.first_login = 0
            db.session.add(VenueType(venue_type="INSIDE", user_id=current_user.user_id))
            db.session.add(VenueType(venue_type="OUTSIDE", user_id=current_user.user_id))
            db.session.add(BookingStatus(booking_status="Active", user_id=current_user.user_id))
            db.session.add(BookingStatus(booking_status="Cancelled", user_id=current_user.user_id))
            db.session.add(BookingStatus(booking_status="Delayed", user_id=current_user.user_id))
            db.session.commit()
            return "Signal received by Flask", 200
    elif request.method == "GET" and current_user.first_login:
        return render_template("new_business.html", title="Business Startup", business_form=business_form, artist_form=artist_form, artist_main_form=artist_main_form)
    else:
        return redirect(url_for("main.home"))


@business_add.route("/businessname", methods=["GET", "POST"])
@login_required
def business_name():
    business_form = BusinessForm()
    business_form.business_name.data = current_user.business_name
    if request.method == 'POST':
        current_user.business_name = request.form.get('business_name')
        db.session.commit()
        return "Data saved successfully!", 200
    return render_template("businessname.html", business_form=business_form)


@business_add.route("/newartist", methods=['GET', 'POST'])
@login_required
def new_artist():
    artist_main_form = ArtistMainForm()
    artist_form = ArtistForm()
    if request.method == 'POST':
        if current_user.first_login:
            artist = Artist(artist_name=artist_main_form.artist_name.data, artist_number=artist_main_form.artist_number.data, user_id=current_user.user_id)
            db.session.add(artist)
            db.session.commit()
            artist_count = int(request.form.get('artistCount'))
            if artist_count > 0:
                for i in range(1, artist_count + 1):
                    artist = Artist(artist_name=request.form.get(f'artist_name_{i}'),
                                    artist_number=request.form.get(f'artist_number_{i}'),
                                    user_id=current_user.user_id)
                    db.session.add(artist)
                    db.session.commit()
            return "Data saved successfully!", 200
        else:
            artist = Artist(artist_name=artist_form.artist_name.data, artist_number=artist_form.artist_number.data, user_id=current_user.user_id)
            db.session.add(artist)
            db.session.commit()
            flash("Artist Added Successfully", "success")
            return redirect(url_for("main.business"))
    elif request.method == "GET":
        legend = "Add New Artist"
        return render_template("artist.html", form=artist_form, legend = legend)

@business_add.route("/newschedule", methods=['POST'])
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


@business_add.route("/newpackage", methods=['GET', 'POST'])
@login_required
def new_package():
    form = PackageForm()
    if request.method == 'POST':
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
    elif request.method == "GET":
        return render_template("package_type.html", form=form)
        

@business_add.route("/neweventtype", methods=['POST'])
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


@business_add.route("/newpaymentmethod", methods=['POST'])
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


