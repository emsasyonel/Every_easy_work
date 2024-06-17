import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "emrebayramsaat@gmail.com"

mesaj["To"] = "elifsultansaat@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = len("""

Smtp ile mail gönderiyorum 

""")

mesaj_gövdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_gövdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("emrebayramsaat@gmail.com","Emre123456789!")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi..")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()