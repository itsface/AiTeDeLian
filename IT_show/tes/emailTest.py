import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey="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")
from_email = Email("ITshow@ITouc.com")#Email("test@example.com")
to_email = Email("983739298@qq.com")
subject = "一个邮件"
content = Content("text/plain", "发一个邮件试试")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)