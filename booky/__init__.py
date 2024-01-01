from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import event
from flask_bcrypt import Bcrypt
from booky.config import Config

# Create the Flask app instance

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

from booky.users.routes import users
from booky.main.routes import main
from booky.business_add.routes import business_add
from booky.business_edit.routes import business_edit



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(business_add)
    app.register_blueprint(business_edit)

    # Function to execute pragma on connect
    def activate_foreign_keys(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    # Attach the event listener to the SQLAlchemy engine
    with app.app_context():
        event.listen(db.engine, 'connect', activate_foreign_keys)

    return app