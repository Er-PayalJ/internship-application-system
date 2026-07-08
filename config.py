class Config:
    SECRET_KEY = "internship_secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:toor@localhost/internship_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "uploads"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "dikshamd17@gmail.com"
    MAIL_PASSWORD = "indianarmy1600"