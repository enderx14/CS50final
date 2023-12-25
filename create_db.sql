PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS "users"
(
   [UserId] INTEGER NOT NULL,
   [UserName] VARCHAR(20) NOT NULL,
   [Email] VARCHAR(120) NOT NULL,
   [Password] VARCHAR(60) NOT NULL,
   [ImageFile] VARCHAR(20) NOT NULL,
   [CreatedAt] DATETIME NOT NULL,
   PRIMARY KEY (UserId), 
   UNIQUE (UserName), 
   UNIQUE (Email)
)

CREATE TABLE IF NOT EXISTS "clients"
(
    [ClientId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [UserId] INTEGER NOT NULL,
    [FirstName] TEXT NOT NULL,
    [LastName] TEXT  NOT NULL,
    [PrimaryPhone] TEXT NOT NULL UNIQUE,
    [SecondaryPhone] TEXT,
    [WhatsAppNumber] TEXT,
    [BookingId] INTEGER,
    FOREIGN KEY (UserId)
    REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
    FOREIGN KEY (BookingId)
    REFERENCES bookings (BookingId)
       ON UPDATE NO ACTION
       ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "bookings"
(
   [BookingId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [BookingStatusId] INTEGER NOT NULL,
   [PackageTypeId] INTEGER NOT NULL,
   [ArtistId] INTEGER NOT NULL,
   [ArtistConfirmed] INTEGER DEFAULT 1
   [EventDate] TEXT NOT NULL,
   [EventTypeId] INTEGER NOT NULL,
   [VenueTypeId] INTEGER NOT NULL,
   [VenueId] INTEGER NOT NULL,
   [VenueNotes] TEXT,
   [ScheduleId] INTEGER NOT NULL,
   [CustomSchedule] TEXT,
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
   FOREIGN KEY (EventTypeId)
   REFERENCES event_types(EventTypeId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT,
   FOREIGN KEY (VenueTypeId)
   REFERENCES venue_types(VenueTypeId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT,
   FOREIGN KEY (VenueId)
   REFERENCES venues(VenueId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT,
   FOREIGN KEY (ScheduleId)
   REFERENCES schedules(ScheduleId)
      ON DELETE NO ACTION
      ON UPDATE CASCADE,
   FOREIGN KEY (BookingStatusId)
   REFERENCES bookingstatus(BookingStatusId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT,
   FOREIGN KEY (PackageTypeId)
   REFERENCES packagetypes(PackageTypeId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT,
   FOREIGN KEY (ArtistId)
   REFERENCES artists(ArtistId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT
);

CREATE TABLE IF NOT EXISTS "client_ledger"
(
   [ClientLedgerId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [ClientId] INTEGER  NOT NULL,
   [UserId] INTEGER NOT NULL,
   [BookingId] INTEGER NOT NULL,
   [TotalCost] INTEGER NOT NULL,
   [TotalPayments] INTEGER NOT NULL,
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
   FOREIGN KEY (ClientId)
   REFERENCES clients(ClientId)
   FOREIGN KEY (BookingId)
   REFERENCES bookings(BookingId)
);

CREATE TABLE IF NOT EXISTS "transactions"
(
   [TransactionId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [TransactionDate] TEXT NOT NULL,
   [Amount] INTEGER NOT NULL,
   [PaymentMethodId] INTEGER NOT NULL,
   [ClientId] INTEGER  NOT NULL,
   [BookingId] INTEGER  NOT NULL,
   [PaymentDetail] TEXT,
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
   FOREIGN KEY (PaymentMethodId)
   REFERENCES payment_methods(PaymentMethodId)
      ON DELETE RESTRICT
      ON UPDATE RESTRICT,
   FOREIGN KEY (ClientId)
   REFERENCES clients(ClientId)
   FOREIGN KEY (BookingId)
   REFERENCES bookings(BookingId)
);

CREATE TABLE IF NOT EXISTS "bookingstatus"
(
   [BookingStatusId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [BookingStatus] TEXT UNIQUE DEFAULT 'Active',
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "packagetypes"
(
   [PackageTypeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [PackageType] TEXT UNIQUE DEFAULT 'Makeup Only',
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "artists"
(
   [ArtistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [ArtistName] TEXT UNIQUE DEFAULT 'Safaa Kandil',
   [ArtistNumber] TEXT UNIQUE DEFAULT '01091177614',
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "event_types"
(
   [EventTypeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [EventType] TEXT UNIQUE DEFAULT,
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "venues"
(
   [VenueId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [VenueName] TEXT UNIQUE DEFAULT SK,
   [VenueLocation] TEXT,
   [VenueDetail] TEXT,
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "venue_types"
(
   [VenueTypeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [VenueType] TEXT UNIQUE DEFAULT 'INSIDE',
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
);

CREATE TABLE IF NOT EXISTS "schedules"
(
   [ScheduleId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [Schedule] TEXT UNIQUE,
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "payment_methods"
(
   [PaymentMethodId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   [UserId] INTEGER NOT NULL,
   [PaymentMethod] TEXT UNIQUE DEFAULT 'Mobile Wallet',
   FOREIGN KEY (UserId)
   REFERENCES users(UserId)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);

CREATE INDEX idx_clients_primaryphone ON clients(PrimaryPhone);
CREATE INDEX idx_bookings_eventdate ON bookings(EventDate);
CREATE INDEX idx_clientledger_bookingid ON client_ledger(BookingId);
CREATE INDEX idx_transactions_bookingid ON transactions(BookingId);