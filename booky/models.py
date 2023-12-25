from datetime import datetime
from booky import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    business_name = db.Column(db.String(120))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    first_login = db.Column(db.Integer, default=0)

    __table_args__ = (
        db.Index('idx_username_email', 'username', 'email'),
    )

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    def get_id(self):
        return str(self.user_id)


class Client(db.Model):
    __tablename__ = "client"
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(90), nullable=False)
    primary_phone = db.Column(db.String(20), nullable=False, unique=True)
    secondary_phone = db.Column(db.String(20))
    whatsapp_number = db.Column(db.String(20))
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.booking_id', onupdate='NO ACTION', ondelete='NO ACTION'))

    # Relationship to User and Booking models
    user = db.relationship('User', backref='clients', lazy=True)
    booking = db.relationship('Booking', backref='clients', lazy=True)

    __table_args__ = (
        db.Index('idx_client_primaryphone', 'primary_phone'),
    )

    def __repr__(self):
        return f"Client(FirstName='{self.first_name}', LastName='{self.last_name}', PrimaryPhone='{self.primary_phone}')"
  

class ClientLedger(db.Model):
    __tablename__ = "clientledger"
    clientledger_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.booking_id'), nullable=False)
    total_cost = db.Column(db.Integer, nullable=False)
    total_payments = db.Column(db.Integer, nullable=False)

    # Relationships to User and Booking models
    user = db.relationship('User', backref='client_ledger', lazy=True)
    booking = db.relationship('Booking', backref='client_ledger', lazy=True)

    __table_args__ = (
        db.Index('idx_clientledger_bookingid', 'booking_id'),
    )

    def __repr__(self):
        return f"ClientLedger(total_cost={self.total_cost}, total_payments={self.total_payments})"


class Transaction(db.Model):
    __tablename__ = "transaction"
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('paymentmethod.payment_method_id'), nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    booking_id = db.Column(db.Integer, nullable=False)
    payment_detail = db.Column(db.Text)

    # Relationships to User and PaymentMethod models
    user = db.relationship('User', backref='transactions', lazy=True)
    paymentmethod = db.relationship('PaymentMethod', backref='transactions', lazy=True)

    __table_args__ = (
        db.Index('idx_transactions_bookingid', 'booking_id'),
    )

    
    def __repr__(self):
        return f"Transaction(transaction_date='{self.transaction_date}', Amount={self.amount})"


class BookingStatus(db.Model):
    __tablename__ = "bookingstatus"
    booking_status_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    booking_status = db.Column(db.String(30), unique=True, default='Active')

    # Relationship to User model
    user = db.relationship('User', backref='booking_status', lazy=True)

    def __repr__(self):
        return f"BookingStatus(BookingStatus='{self.booking_status}')"
    

class PackageType(db.Model):
    __tablename__ = "packagetype"
    package_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    package_type = db.Column(db.String(90), unique=True, default='Makeup Only')
    package_type_detail = db.Column(db.String(200))

    # Relationship to User model
    user = db.relationship('User', backref='package_types', lazy=True)

    def __repr__(self):
        return f"PackageType(package_type='{self.package_type}')"
    

class Artist(db.Model):
    __tablename__ = "artist"
    artist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    artist_name = db.Column(db.String(20), unique=True)
    artist_number = db.Column(db.String(20), unique=True)

    # Relationship to User model
    user = db.relationship('User', backref='artists', lazy=True)

    def __repr__(self):
        return f"Artist(artist_name='{self.artist_name}', artist_number='{self.artist_number}')"


class EventType(db.Model):
    __tablename__ = "eventtype"
    event_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    event_type = db.Column(db.String(30), unique=True, default='Wedding')

    # Relationship to User model
    user = db.relationship('User', backref='event_types', lazy=True)

    def __repr__(self):
        return f"EventType(event_type='{self.event_type}')"


class Venue(db.Model):
    __tablename__ = "venue"
    venue_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    venue_name = db.Column(db.String(60), unique=True, default='SK')
    venue_location = db.Column(db.String(120))
    venue_detail = db.Column(db.String(120))

    # Relationship to User model
    user = db.relationship('User', backref='venues', lazy=True)

    def __repr__(self):
        return f"Venue(venue_name='{self.venue_name}', venue_location='{self.venue_location}', venue_detail='{self.venue_detail}')"


class VenueType(db.Model):
    __tablename__ = "venuetype"
    venue_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    venue_type = db.Column(db.String(20), unique=True, default='INSIDE')

    # Relationship to User model
    user = db.relationship('User', backref='venue_types', lazy=True)

    def __repr__(self):
        return f"VenueType(venue_type='{self.venue_type}')"


class PaymentMethod(db.Model):
    __tablename__ = 'paymentmethod'
    payment_method_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    payment_method = db.Column(db.String(120), unique=True, default='Mobile Wallet')

    user = db.relationship('User', backref='payment_methods', lazy=True)

    def __repr__(self):
        return f"PaymentMethod(payment_method='{self.payment_method}')"
    

class Schedule(db.Model):
    __tablename__ = "schedule"
    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    schedule = db.Column(db.String(20), unique=True, nullable=False)

    user = db.relationship('User', backref='schedules', lazy=True)

    def __repr__(self):
        return f"Schedule(schedule='{self.schedule}')"


class Booking(db.Model):
    __tablename__ = "booking"
    booking_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    booking_status_id = db.Column(db.Integer, db.ForeignKey('bookingstatus.booking_status_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    package_type_id = db.Column(db.Integer, db.ForeignKey('packagetype.package_type_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    artist_confirmed = db.Column(db.Integer, default=1)
    event_date = db.Column(db.DateTime, nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('eventtype.event_type_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    venue_type_id = db.Column(db.Integer, db.ForeignKey('venuetype.venue_type_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    venue_notes = db.Column(db.Text)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.schedule_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    custom_schedule = db.Column(db.String(30))

    # Relationships to other models
    user = db.relationship('User', backref='bookings', lazy=True)
    eventtype = db.relationship('EventType', backref='bookings', lazy=True)
    venuetype = db.relationship('VenueType', backref='bookings', lazy=True)
    venue = db.relationship('Venue', backref='bookings', lazy=True)
    schedule = db.relationship('Schedule', backref='bookings', lazy=True)
    bookingstatus = db.relationship('BookingStatus', backref='bookings', lazy=True)
    packagetype = db.relationship('PackageType', backref='bookings', lazy=True)
    artist = db.relationship('Artist', backref='bookings', lazy=True)

    __table_args__ = (
        db.Index('idx_booking_eventdate', 'event_date'),
    )

    def __repr__(self):
        return f"Booking(event_date='{self.event_date}')"
  