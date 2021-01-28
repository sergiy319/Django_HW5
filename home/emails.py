from django.conf import settings
from django.core.mail import send_mail


# Create a function for sending email.
def send_email(recipient_list=None):
    subject = 'Thank you for registering to our site'

    message = ' it  means a world to us.  '

    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, recipient_list)
