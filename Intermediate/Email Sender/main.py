import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

from cred import EMAIL, PASSWORD


def create_img_attachment(img: str) -> MIMEImage:
    """Attach an image file to the email."""
    with open(img, 'rb') as img_file:
        mime_img = MIMEImage(img_file.read())
        mime_img.add_header('Content-Disposition', 'attachment', filename=img)
        return mime_img


def send_email(to_email: str, subject: str, body: str, img: str) -> None:
    """Send an email using Gmail's SMTP server."""
    host: str = 'smtp.gmail.com'
    port: int = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(EMAIL, PASSWORD)

        print(f'Sending email to {to_email}')

        message = MIMEMultipart()
        message['From'] = EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if img:
            file: MIMEImage = create_img_attachment(img)
            message.attach(file)

        server.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=message.as_string())

        print('Email sent!')


if __name__ == '__main__':
    for i in range(10):
        subject = f"I love you {i}"
        send_email(
            to_email="mollikamukta87@gmail.com",
            subject=subject,
            body="Hello there, How are you?",
            img="cat.png"
        )
        time.sleep(5)

