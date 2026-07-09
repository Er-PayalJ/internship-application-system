from flask import Blueprint, request, jsonify
from extensions import db
from models import Admin, Application
from werkzeug.security import check_password_hash
from email_utils import send_status_email

admin_bp = Blueprint("admin", __name__)


# ==========================
# Admin Login
# ==========================
@admin_bp.route("/admin/login", methods=["POST"])
def admin_login():

    data = request.json

    username = data["username"]
    password = data["password"]

    admin = Admin.query.filter_by(username=username).first()

    if admin is None:
        return jsonify({"message": "Invalid Username"})

    if check_password_hash(admin.password, password):

        return jsonify({"message": "Login Successful"})

    return jsonify({"message": "Wrong Password"})


# ==========================
# View Applications
# ==========================
@admin_bp.route("/admin/applications", methods=["GET"])
def applications():

    apps = Application.query.all()

    data = []

    for app in apps:

        data.append({

            "Application_ID": app.id,
            "Student": app.student.name,
            "Email": app.student.email,
            "Company": app.company.company_name,
            "Role": app.company.internship_role,
            "Status": app.status,
            "Resume": app.resume

        })

    return jsonify(data)


# ==========================
# Accept Application
# ==========================
@admin_bp.route("/admin/accept/<int:id>", methods=["PUT"])
def accept(id):

    app = Application.query.get(id)

    if app is None:
        return jsonify({"message": "Application Not Found"})

    app.status = "Accepted"

    db.session.commit()

    send_status_email(app.student.email, "Accepted")

    return jsonify({"message": "Application Accepted"})


# ==========================
# Reject Application
# ==========================
@admin_bp.route("/admin/reject/<int:id>", methods=["PUT"])
def reject(id):

    app = Application.query.get(id)

    if app is None:
        return jsonify({"message": "Application Not Found"})

    app.status = "Rejected"

    db.session.commit()

    send_status_email(app.student.email, "Rejected")

    return jsonify({"message": "Application Rejected"})