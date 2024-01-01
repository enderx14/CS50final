from booky import create_app, db

app = create_app()
# Ensure this code runs within the Flask app context
with app.app_context():
    # Create all tables
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
