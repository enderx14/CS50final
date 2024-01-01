# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, TextAreaField, FieldList
# from wtforms.validators import InputRequired


# class BookingForm(FlaskForm):
#     title = StringField('Title', validators=[InputRequired()])
#     content = TextAreaField('Content', validators=[InputRequired()])
#     submit = SubmitField('Add Booking')


# class BusinessForm(FlaskForm):
#     business_name = StringField('Business Name', validators=[InputRequired()])
#     submit = SubmitField('Add Business')


# class ArtistMainForm(FlaskForm):
#     artist_name = StringField('Main Artist Name', validators=[InputRequired()])
#     artist_number = StringField('Main Artist Number', validators=[InputRequired()])
#     submit = SubmitField('Save Artists')

# class ArtistForm(FlaskForm):
#     artist_id = StringField('Artist ID]')
#     artist_name = StringField('Artist Name', validators=[InputRequired()])
#     artist_number = StringField('Artist Number', validators=[InputRequired()])
#     submit = SubmitField('Save Artists')


# class PackageForm(FlaskForm):
#     package_type = StringField('Package', validators=[InputRequired()])
#     package_type_detail = TextAreaField('Package Details')
#     submit = SubmitField('Save Packages')


# class ScheduleForm(FlaskForm):
#     # schedule = StringField('Schedule', validators=[InputRequired()])
#     schedules = FieldList(StringField('Schedules'), min_entries=3)
#     submit = SubmitField('Save Schedules')


# class PaymentMethodForm(FlaskForm):
#     payment_method = StringField('Payment Method', validators=[InputRequired()])
#     submit = SubmitField('Add Payment Method')


# class EventTypeForm(FlaskForm):
#     event_type = StringField('Event Type', validators=[InputRequired()])
#     submit = SubmitField('Add Event Type')


# class VenueTypeForm(FlaskForm):
#     venue_type = StringField('Venue Type', validators=[InputRequired()])
#     submit = SubmitField('Add Venue Type')