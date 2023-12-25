from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import event
from flask_bcrypt import Bcrypt

# Create the Flask app instance
app = Flask(__name__)

# Create the Flask app Secret Key
app.config["SECRET_KEY"] = "3bbbb0dd99b4f08da462e382d76660ac"

# Configure the SQLite database with SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///booky.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

with app.app_context():
    # Function to execute pragma on connect
    def activate_foreign_keys(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    # Attach the event listener to the SQLAlchemy engine
    event.listen(db.engine, 'connect', activate_foreign_keys)

from booky import routes
