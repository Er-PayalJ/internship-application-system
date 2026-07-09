from extensions import db
from datetime import datetime


# ==========================
# Student Table
# ==========================

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    mobile = db.Column(db.String(15), nullable=False)

    password = db.Column(db.String(200), nullable=False)

    otp = db.Column(db.String(6))

    verified = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ==========================
# Company Table
# ==========================

class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(100))

    internship_role = db.Column(db.String(100))

    stipend = db.Column(db.String(50))


# ==========================
# Internship Application
# ==========================

class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey('students.id'),
        nullable=False
    )

    company_id = db.Column(
        db.Integer,
        db.ForeignKey('companies.id'),
        nullable=False
    )

    resume = db.Column(db.String(200))

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    applied_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    student = db.relationship(
        "Student",
        backref="applications"
    )

    company = db.relationship(
        "Company",
        backref="applications"
    )


# ==========================
# Admin Table
# ==========================

class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )