from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from extensions import db
from models import Company, Application
import os

student_bp = Blueprint("student", __name__)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ======================================
# View Companies
# ======================================
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


# ======================================
# Apply Internship
# ======================================
@student_bp.route("/apply", methods=["POST"])
def apply():

    student_id = request.form.get("student_id")
    company_id = request.form.get("company_id")
    resume = request.files.get("resume")

    if not student_id or not company_id or resume is None:
        return jsonify({
            "message": "All fields are required."
        }), 400

    # Prevent duplicate application
    existing = Application.query.filter_by(
        student_id=student_id,
        company_id=company_id
    ).first()

    if existing:
        return jsonify({
            "message": "You have already applied to this company."
        }), 400

    # Resume validation
    if resume.filename == "":
        return jsonify({
            "message": "Please select a resume."
        }), 400

    if not allowed_file(resume.filename):
        return jsonify({
            "message": "Only PDF, DOC and DOCX files are allowed."
        }), 400

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filename = secure_filename(resume.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    resume.save(filepath)

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


# ======================================
# My Application Status
# ======================================
@student_bp.route("/status/<int:id>", methods=["GET"])
def status(id):

    applications = Application.query.filter_by(student_id=id).all()

    result = []

    for app in applications:

        result.append({
            "application_id": app.id,
            "company": app.company.company_name,
            "role": app.company.internship_role,
            "location": app.company.location,
            "stipend": app.company.stipend,
            "status": app.status,
            "resume": app.resume
        })

    return jsonify(result)