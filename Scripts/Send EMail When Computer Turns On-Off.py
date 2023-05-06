import datetime
import smtplib
import ssl
from email.message import EmailMessage


def sendMail(sender_email, password, receiver_email):
    # Get the current date and time
    date = str(datetime.datetime.now().strftime('%d/%m/%Y'))
    time = str(datetime.datetime.now().strftime('%H:%M'))

    # Create te Subject and the Body
    subject = "ON/OFF PC Status"
    body = F'Computer Status: ON \n {time} \n {date}'
    # body = F'Computer Status: OFF \n {time} \n {date}'

    # Create an instance of EmailMessage
    email_message = EmailMessage()

    # Set the "From", "To", "Subject" and "Body" fields of the email message
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    email_message.set_content(body)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to Gmail's SMTP server using SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        # Login to the sender's account using the provided credentials
        smtp.login(sender_email, password)

        # Send the email message to the receiver
        smtp.sendmail(sender_email, receiver_email, email_message.as_string())

        # Print a message to indicate that the email has been sent successfully
        print(F"Successfully sent email to: {email_message['To']}")


# Run gpedit.msc
# Computer Configuration -> Windows Settings -> Scripts -> Shutdown -> Properties -> Add

# You must use the password from: https://myaccount.google.com/apppasswords
sendMail("mail1@gmail.com",
         "password123",
         "mail2@gmail.com")
