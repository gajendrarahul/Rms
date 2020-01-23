from django.core.mail import send_mail
from django.conf import settings
class Mail:
    email_form = settings.EMAIL_HOST
    def __init__(self,subject="LMS system", message=None,recipient_list=None):
        try:
            print("-----------------try for mail----------------")
            send_mail(subject,message,self.email_form,recipient_list)
        except:
            return "Error occured"