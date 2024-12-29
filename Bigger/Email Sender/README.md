# Email Sender with Attachment

This Python script allows you to send emails with an image attachment using Gmail's SMTP server. The script uses `smtplib` for sending emails and `email.mime` modules for formatting and attaching files.

## Features

- Send an email using Gmail's SMTP server.
- Attach an image file to the email.
- Customize the subject, body, and recipient email.
- Secure login with environment variables for email credentials.

## Requirements

Before running the script, make sure you have the following dependencies installed:

- Python 3.7 or higher
- `python-dotenv` library for loading environment variables

You can install the required dependencies with pip:

```bash
pip install python-dotenv
```

## Setup

1. **Create an `.env` file** in the root directory of your project and add your email credentials as follows:

   ```ini
   EMAIL=your_email@gmail.com
   PASSWORD=your_email_password
   ```

   **Important**: Use an App Password if you're using Gmail with 2-step verification enabled. You can generate one [here](https://myaccount.google.com/apppasswords).

2. **Prepare the image** that you want to send as an attachment. The script expects an image file named `cat.png` (or replace it with any valid file name you prefer).

3. **Run the script**:

   Once the setup is complete, run the Python script to send the email:

   ```bash
   python email_sender.py
   ```

   The script will send two emails with the subject "Hello Moon 0" and "Hello Moon 1" to the specified recipient with the attached image.

## Code Overview

- **Environment Variables**: The script loads email credentials from a `.env` file using `python-dotenv` for security.
- **SMTP**: It connects to Gmail's SMTP server (`smtp.gmail.com`), uses TLS encryption, and logs in with the provided email and password.
- **MIME**: The script creates a multipart email with the subject, body, and optional image attachment.
- **Image Attachment**: The function `create_img_attachment()` handles reading and attaching an image to the email.

## License

This project is licensed under the MIT License

