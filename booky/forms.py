from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FieldList
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from booky.models import User

class RegisterationForm(FlaskForm):
    username = StringField("Username",
                           validators=[InputRequired(message='Username is required.'),
                                       Length(min=4, max=20, message="Username must be between %(min)d and %(max)d ")])
    email = StringField("Email",
                        validators=[InputRequired(message='Email is required.'), Email()])
    password = PasswordField("Password",
                             validators=[InputRequired(message='Password is required.'),
                                         Length(min=8, max=16, message="Password must be between %(min)d and %(max)d ")])
    confirm_password = PasswordField("Confirm Password",
                             validators=[InputRequired(message='Password is required.'), Length(min=8, max=12),
                             EqualTo("password", message='Passwords must match')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is already taken, Please choose another one ")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already registered, Please choose another one ")


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[InputRequired(message='Email is required.'), Email()])
    password = PasswordField("Password",
                             validators=[InputRequired(message='Password is required.')])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    username = StringField("Username",
                           validators=[InputRequired(message='Username is required.'),
                                       Length(min=4, max=20, message="Username must be between %(min)d and %(max)d ")])
    email = StringField("Email",
                        validators=[InputRequired(message='Email is required.'), Email()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username is already taken, Please choose another one ")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email is already registered, Please choose another one ")

class BookingForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = TextAreaField('Content', validators=[InputRequired()])
    submit = SubmitField('Add Booking')


class BusinessForm(FlaskForm):
    business_name = StringField('Business Name', validators=[InputRequired()])
    submit = SubmitField('Add Business')


class ArtistMainForm(FlaskForm):
    artist_name = StringField('Main Artist Name', validators=[InputRequired()])
    artist_number = StringField('Main Artist Number', validators=[InputRequired()])
    submit = SubmitField('Save Artists')

class ArtistForm(FlaskForm):
    artist_id = StringField('Artist ID]')
    artist_name = StringField('Artist Name', validators=[InputRequired()])
    artist_number = StringField('Artist Number', validators=[InputRequired()])
    submit = SubmitField('Save Artists')


class PackageForm(FlaskForm):
    package_type = StringField('Package', validators=[InputRequired()])
    package_type_detail = TextAreaField('Package Details')
    submit = SubmitField('Save Packages')


class ScheduleForm(FlaskForm):
    # schedule = StringField('Schedule', validators=[InputRequired()])
    schedules = FieldList(StringField('Schedules'), min_entries=3)
    submit = SubmitField('Save Schedules')


class PaymentMethodForm(FlaskForm):
    payment_method = StringField('Payment Method', validators=[InputRequired()])
    submit = SubmitField('Add Payment Method')


class EventTypeForm(FlaskForm):
    event_type = StringField('Event Type', validators=[InputRequired()])
    submit = SubmitField('Add Event Type')


class VenueTypeForm(FlaskForm):
    venue_type = StringField('Venue Type', validators=[InputRequired()])
    submit = SubmitField('Add Venue Type')