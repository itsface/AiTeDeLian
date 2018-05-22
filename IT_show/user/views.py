from django.shortcuts import render
from random import Random
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


def sendEmail(name, code, mail,text):
        try:
            send_mail(
                '爱特工作室',
                '' + name + '同学,你好！\n'
                            +text+
                            '\n你的个人ID为:' + code+'\n',
                'easyblog123@163.com',
                [mail],
                fail_silently=False
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found')