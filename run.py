from booky import app, db

# Ensure this code runs within the Flask app context
with app.app_context():
    # Create all tables
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
