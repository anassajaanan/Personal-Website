from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        send_mail(name, email, subject, message)
        return "Your message has been sent. Thank you!"
    return render_template('index.html')

@app.route('/work', methods=['GET'])
def work():
    num = request.args.get('num')
    return render_template(f'portfolio-details{num}.html')

MY_EMAIL = os.environ.get('EMAIL')
MY_PASSWORD = os.environ.get('PASSWORD')

def send_mail(name, email, subject, message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="anasajaanan.official@gmail.com",
        msg=f"Subject:Contact from MorseCode\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}.".encode('UTF-8')
    )

if __name__ == '__main__':
    app.run()
