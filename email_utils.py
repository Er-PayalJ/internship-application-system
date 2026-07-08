import random
from flask_mail import Message
from extensions import mail


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):
    msg = Message(
        subject="Internship Portal OTP Verification",
        sender="yourgmail@gmail.com",
        recipients=[email]
    )

    msg.body = f"""
Hello Student,

Your OTP for Internship Portal Verification is:

{otp}

Do not share this OTP with anyone.

Thank You
Internship Portal
"""

    mail.send(msg)


def send_status_email(email, status):

    msg = Message(
        subject="Internship Application Status",
        sender="yourgmail@gmail.com",
        recipients=[email]
    )

    msg.body = f"""
Your Internship Application has been

{status}

Thank You
"""

    mail.send(msg)