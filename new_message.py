import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email_with_attachment(frame):
    # Email configurations
    sender_email = "saigopalvallu7@gmail.com"
    receiver_email = "gopalvalluintern@gmail.com"
    password = "wwlh wrpw jlvz yoad"

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Accident Detected!"

    # Attach the frame as an image
    img = MIMEImage(frame, name='accident_frame.jpg')
    msg.attach(img)

    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")

# Modify your code to use this function
