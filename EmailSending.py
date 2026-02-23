
import smtplib

from email.message import EmailMessage

def send_mail(sender, password, receiver, subject, body):
    
    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set Mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add Email Body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + Password
    smtp.login(sender, password)

    # Step 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close the connection manually
    smtp.quit()


def main():
    
    # Sender Email
    sender_email = "umesh.example@gmail.com"

    app_password = "Enter your app password here"

    receiver_email = "jhondoe.example@gmail.com"

    subject = "Test Mail from Python Script"

    body = """Jay Ganesh,

    This is a test email sent using Python.

    Regards,
    Umesh Bhabad
    """

    send_mail(sender_email, app_password, receiver_email, subject, body)

    print("Mail sent sucessfully")

if __name__ == "__main__":
    main()