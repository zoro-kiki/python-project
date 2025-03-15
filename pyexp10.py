#ZAARA 231P023
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send email
def send_email(sender_email, receiver_email, subject, body, password):
    # Create the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail's SMTP server
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

        # Close the server connection
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Replace with your credentials and email details
sender_email = "zaarakhn07@eng.rizvi.edu.in"
receiver_email = "zaarakhn07@eng.rizvi.edu.in"
subject = "Test Email"
body = "Hello, this is a test email from Python!"
password = "***"  # Use your Gmail password

# Call the function to send the email
send_email(sender_email, receiver_email, subject, body, password)


