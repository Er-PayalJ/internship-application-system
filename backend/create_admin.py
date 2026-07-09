from app import app
from extensions import db
from models import Admin
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = Admin(
        username="root",
        password=generate_password_hash("toor")
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin Created Successfully")