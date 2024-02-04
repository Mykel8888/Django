import yagmail
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(subject, message, to_email):
    with yagmail.SMTP(settings.YAGMAIL_EMAIL, settings.YAGMAIL_PASSWORD, settings.YAGMAIL_SMTP_FILE) as yag:
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
        yag.send(settings.YAGMAIL_EMAIL, subject, email.message().as_string())