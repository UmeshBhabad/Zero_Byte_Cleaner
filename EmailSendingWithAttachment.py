import os
import smtplib

from email.message import EmailMessage

def send_mail(sender, password, receiver, subject, body, report):
    
    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set Mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add Email Body
    msg.set_content(body)

    # Step 4 : Add attachment
    fobj = open(report, "rb")

    file_data = fobj.read()
    file_name = os.path.basename(report)

    msg.add_attachment (
                        file_data,
                        maintype = "application",
                        subtype = "octet-stream",
                        filename = file_name
                        )

    # Step 5 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 6 : Login using Gmail + Password
    smtp.login(sender, password)

    # Step 7 : Send the email
    smtp.send_message(msg)

    # Step 8 : Close the connection manually
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

    report_path = "LogReport_Mon_Feb_23_02_29_16_2026.log"

    send_mail(sender_email, app_password, receiver_email, subject, body, report_path)

    print("Mail sent sucessfully")

if __name__ == "__main__":
    main()