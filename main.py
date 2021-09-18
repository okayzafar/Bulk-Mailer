import pandas as pd
import smtplib

# reading excel email list + retrieving the values
e = pd.read_excel(r"C:\Users\Siraj\OneDrive\Desktop\emailList.xlsx")
email = e['Email'].values

# setting up server to send mail
# server = smtplib.SMTP("smtp.gmail.com", 587)
server = smtplib.SMTP("localhost", 1025)

#server.starttls()
#server.login("bulkmailer321@gmail.com", "BulkMailer321")
msg = "No matter what genre of beat you're looking for we have it! Check out the latest free beats sourced from the internet."

subject = "Need free beats?"
body = "Subject: {}\n\n{}".format(subject, msg)

# loop to send emails from server to email list
for email in email:
    server.sendmail("bulkmailer321@gmail.com", email, body)
server.quit()
