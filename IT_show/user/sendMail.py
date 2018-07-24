from django.core.mail import send_mail as core_send_mail
from django.core.mail import EmailMultiAlternatives
import threading
import sendgrid
import os
from sendgrid.helpers.mail import *



class EmailThread(threading.Thread):
    # sg = sendgrid.SendGridAPIClient(apikey="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")
    # from_email = Email("ITStudio@oucIT.com")  # Email("test@example.com")
    # to_email = Email("983739298@qq.com")
    # subject = "爱特工作室"
    # content = Content("text/plain", "用户您好，")
    # mail = Mail(from_email, subject, to_email, content)
    # response = sg.client.mail.send.post(request_body=mail.get())

    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        threading.Thread.__init__(self)
        self.subject = subject
        self.body =Content("text/plain", body)
        self.recipient_list = Email(recipient_list)
        self.from_email = Email(from_email)
        self.fail_silently = fail_silently
        self.html = html


    def run (self):
        sg = sendgrid.SendGridAPIClient(apikey="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")
        mail = Mail("ITStudio@oucIT.com", self.subject, self.recipient_list, self.body)
        response = sg.client.mail.send.post(request_body=mail.get())
        # msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        # if self.html:
        #     msg.attach_alternative(self.html, "text/html")
        # msg.send(self.fail_silently)

def send_mail(subject, body, from_email, to_email, fail_silently=False, html=None, *args, **kwargs):
    try:
        sg = sendgrid.SendGridAPIClient(apikey="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")
        from_email = Email("ITStudio@oucIT.com")  # Email("test@example.com")
        to_email = Email(to_email)
        subject = "爱特工作室"
        content = Content("text/plain", body)
        mail = Mail(from_email, subject, to_email, content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        # EmailThread(subject, body, from_email, to_email, fail_silently, html).start()
    except:
        try:
            core_send_mail(subject, body, from_email, [to_email], fail_silently, html)
        except:
            pass

