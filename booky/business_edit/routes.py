from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_required
from booky import db
from booky.models import Artist, PackageType
from booky.business_add.forms import ArtistForm, PackageForm


business_edit = Blueprint("business_edit", __name__)


@business_edit.route("/artist/<int:artist_id>/update", methods=['GET', 'POST'])
@login_required
def update_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    form = ArtistForm()
    if request.method == "POST":
        artist.artist_name = form.artist_name.data
        artist.artist_number = form.artist_number.data
        db.session.commit()
        flash('Your Artist information has been updated!', 'success')
        return redirect(url_for('main.business'))
    elif request.method == "GET":
        form.artist_name.data = artist.artist_name
        form.artist_number.data = artist.artist_number
        legend = "Update Artist Information"
        return render_template("artist.html", form=form, legend=legend)
    

@business_edit.route("/artist/<int:artist_id>/delete", methods=['POST'])
@login_required
def delete_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    db.session.delete(artist)
    db.session.commit()
    flash('Artist has been deleted!', 'success')
    return redirect(url_for('main.business'))



@business_edit.route("/package_type/<int:package_type_id>/update", methods=['GET', 'POST'])
@login_required
def update_package_type(package_type_id):
    package_type = PackageType.query.get_or_404(package_type_id)
    form = PackageForm()
    if request.method == "POST":
        package_type.package_type = form.package_type.data
        package_type.package_type_detail = form.package_type_detail.data
        db.session.commit()
        flash('Your Package Type information has been updated!', 'success')
        return redirect(url_for('main.business'))
    elif request.method == "GET":
        form.package_type.data = package_type.package_type
        form.package_type_detail.data = package_type.package_type_detail
        legend = "Update Package Type Information"
        return render_template("package_type.html", form=form, legend=legend)
    

@business_edit.route("/package_type/<int:package_type_id>/delete", methods=['POST'])
@login_required
def delete_package_type(package_type_id):   
    package_type = PackageType.query.get_or_404(package_type_id)
    db.session.delete(package_type)
    db.session.commit()
    flash('Package Type has been deleted!', 'success')
    return redirect(url_for('main.business'))