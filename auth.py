from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, jsonify
from extensions import db
from models import Student
from email_utils import generate_otp, send_otp_email

auth_bp = Blueprint("auth", __name__)


# ------------------------
# Register
# ------------------------
@auth_bp.route("/student/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.form

    name = data["name"]
    email = data["email"]
    mobile = data["mobile"]
    password = data["password"]

    student = Student.query.filter_by(email=email).first()

    if student:
        return jsonify({"message": "Email Already Registered"}), 400

    otp = generate_otp()

    new_student = Student(
        name=name,
        email=email,
        mobile=mobile,
        password=generate_password_hash(password),
        otp=otp,
        verified=False
    )

    db.session.add(new_student)
    db.session.commit()

    send_otp_email(email, otp)

    return jsonify({
        "message": "Registration Successful. OTP Sent."
    })


# ------------------------
# Verify OTP
# ------------------------
@auth_bp.route("/verify", methods=["POST"])
def verify():

    data = request.json

    email = data["email"]
    otp = data["otp"]

    student = Student.query.filter_by(email=email).first()

    if student is None:
        return jsonify({"message": "Student Not Found"})

    if student.otp == otp:

        student.verified = True
        student.otp = ""

        db.session.commit()

        return jsonify({"message": "Account Verified"})

    return jsonify({"message": "Invalid OTP"})


# ------------------------
# Login
# ------------------------
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data["email"]
    password = data["password"]

    student = Student.query.filter_by(email=email).first()

    if student is None:
        return jsonify({"message": "Invalid Email"})

    if student.verified is False:
        return jsonify({"message": "Verify OTP First"})

    if check_password_hash(student.password, password):

        return jsonify({
            "message": "Login Successful",
            "student_id": student.id,
            "name": student.name
        })

    return jsonify({"message": "Wrong Password"})











