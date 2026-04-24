import smtplib
import os
from datetime import datetime

class NotificationService:
    def __init__(self):
        # Resolvendo AP-001: Usando variáveis de ambiente
        self.email_host = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
        self.email_port = int(os.getenv('EMAIL_PORT', 587))
        self.email_user = os.getenv('EMAIL_USER')
        self.email_password = os.getenv('EMAIL_PASS')

    def send_email(self, to, subject, body):
        if not self.email_user or not self.email_password:
            print("Configuração de e-mail ausente. Ignorando envio.")
            return False
        try:
            server = smtplib.SMTP(self.email_host, self.email_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(self.email_user, to, message.encode('utf-8'))
            server.quit()
            return True
        except Exception as e:
            print(f"Erro ao enviar email: {str(e)}")
            return False
