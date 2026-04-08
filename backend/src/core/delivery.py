import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import settings


class SMTPClient:
    def __init__(self):
        self.host = settings.SMTP_HOST
        self.port = settings.SMTP_PORT
        self.user = settings.SMTP_USER
        self.password = settings.SMTP_PASS

    def send_email(self, to_email: str, subject: str, body: str, is_html: bool = False):
        msg = MIMEMultipart()
        msg["From"] = self.user
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "html" if is_html else "plain"))

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            if self.user and self.password:
                server.login(self.user, self.password)
            server.send_message(msg)
