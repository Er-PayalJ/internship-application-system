from flask import Flask, render_template
from flask_cors import CORS

from config import Config
from extensions import db, mail

from routes.auth import auth_bp
from routes.student import student_bp
from routes.admin import admin_bp

# ===========================
# Create Flask App
# ===========================
app = Flask(__name__)

# Enable CORS
CORS(app)

# Load Configuration
app.config.from_object(Config)

# Initialize Database and Mail
db.init_app(app)
mail.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(student_bp)
app.register_blueprint(admin_bp)

# Create Database Tables
with app.app_context():
    db.create_all()

# ===========================
# Home Page
# ===========================
@app.route("/")
def home():
    return render_template("index.html")

# ===========================
# Run Application
# ===========================
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)