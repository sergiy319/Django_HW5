from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


# Create a function for sending email.
def send_email(recipient_list=None, activate_url=None):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us.  '
    email_from = settings.EMAIL_HOST_USER

    template = get_template('send_email_test.html')

    send_mail(subject, message, email_from, recipient_list,
              html_message=template.render(context={
                  "activate_url": activate_url,
              }))

