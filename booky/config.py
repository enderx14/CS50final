class Config:
  # Create the Flask app Secret Key
  SECRET_KEY = "3bbbb0dd99b4f08da462e382d76660ac"

  # Configure the SQLite database with SQLAlchemy
  SQLALCHEMY_DATABASE_URI = "sqlite:///booky.db"
  SQLALCHEMY_TRACK_MODIFICATIONS = False 
