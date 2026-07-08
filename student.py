from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from extensions import db
from models import Company, Application
import os

student_bp = Blueprint("student", __name__)

UPLOAD_FOLDER = "uploads"

# ==========================
# View Companies
# ==========================
@student_bp.route("/companies", methods=["GET"])
def companies():

    company_list = Company.query.all()

    data = []

    for c in company_list:

        data.append({

            "id": c.id,
            "company_name": c.company_name,
            "location": c.location,
            "internship_role": c.internship_role,
            "stipend": c.stipend

        })

    return jsonify(data)


# ==========================
# Apply Internship
# ==========================
@student_bp.route("/apply", methods=["POST"])
def apply():

    student_id = request.form["student_id"]
    company_id = request.form["company_id"]

    resume = request.files["resume"]

    filename = secure_filename(resume.filename)

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    resume.save(os.path.join(UPLOAD_FOLDER, filename))

    application = Application(

        student_id=student_id,
        company_id=company_id,
        resume=filename,
        status="Pending"

    )

    db.session.add(application)
    db.session.commit()

    return jsonify({

        "message": "Application Submitted Successfully"

    })


# ==========================
# My Applications
# ==========================
@student_bp.route("/status/<int:id>", methods=["GET"])
def status(id):

    applications = Application.query.filter_by(student_id=id).all()

    result = []

    for app in applications:

        result.append({

            "Application_ID": app.id,
            "Company": app.company.company_name,
            "Role": app.company.internship_role,
            "Status": app.status,
            "Resume": app.resume

        })

    return jsonify(result)