from flask import Blueprint, render_template
from flask_login import login_required
from booky.business_add.forms import ArtistForm, PackageForm


main = Blueprint("main", __name__)


# Define a route for the root URL
@main.route('/')
@main.route('/home')
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


@main.route("/business")
@login_required
def business():
    artist_form = ArtistForm()
    package_form = PackageForm()
    return render_template("business.html", artist_form=artist_form, package_form=package_form)
