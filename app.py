from flask import Flask, request, redirect, render_template, flash, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# 🔐 Email config (Gmail example)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("EMAIL_USER")
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASS")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("EMAIL_USER")

mail = Mail(app)

@app.route('/send', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    msg = Message(
        subject=f"📩 Portfolio Contact: {name}",
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']],
        body=f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""
    )

    mail.send(msg)
    flash("Your message has been sent successfully! 🎉", "success")
    return redirect("/")  # redirect back to homepage

if __name__ == '__main__':
    app.run(debug=True)






