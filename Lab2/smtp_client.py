import smtplib
from email.message import EmailMessage
import logging

logging.basicConfig(filename="smtp_client.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def smtp_client():
    host = input("Enter SMTP server [default smtp.gmail.com]: ").strip() or "smtp.gmail.com"
    port = input("Enter port [default 587]: ").strip() or "587"
    user = input("Enter your email: ").strip()
    pwd = input("Enter password: ").strip()

    to_addr = input("Recipient (comma separated): ").strip()
    recips = [x.strip() for x in to_addr.split(",") if x.strip()] or [user]

    subj = input("Subject [default Test Mail]: ").strip() or "Test Mail"
    text = input("Message body [default Hello]: ").strip() or "Hello, this is a test mail from Python."

    msg = EmailMessage()
    msg["From"] = user
    msg["To"] = ", ".join(recips)
    msg["Subject"] = subj
    msg.set_content(text)

    try:
        logging.info("Connecting to %s:%s", host, port)
        with smtplib.SMTP(host, int(port)) as conn:
            conn.ehlo()
            if int(port) == 587:
                logging.info("Starting TLS encryption")
                conn.starttls()
                conn.ehlo()
            logging.info("Logging in as %s", user)
            conn.login(user, pwd)
            conn.send_message(msg)
            logging.info("Email sent successfully to %s", recips)
            print("Mail delivered to:", ", ".join(recips))
    except Exception as e:
        logging.exception("SMTP process failed")
        print("Unable to send mail:", e)

if __name__ == "__main__":
    smtp_client()
