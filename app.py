from flask import Flask, request, redirect, render_template, flash, url_for
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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



@app.route('/send', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    content = f"""
    New message from your portfolio:

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

        mail = Mail(
            from_email=os.getenv("EMAIL_USER"),  # your email
            to_emails=os.getenv("EMAIL_USER"),
            subject=f"Portfolio Message from {name}",
            plain_text_content=content
        )

        sg.send(mail)

        return redirect(url_for("contact", success=1))

    except Exception as e:
        print("SENDGRID ERROR:", e)
        return redirect(url_for("contact", error=1))

if __name__ == '__main__':
    app.run(debug=True)