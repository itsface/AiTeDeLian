from django.shortcuts import render
from random import Random
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from user.sendMail import send_mail as asynchronousSendEmail
from .form import FresherForm
# Create your views here.


def sendEmail(name, code, mail,text):
        try:
            asynchronousSendEmail(
                '爱特工作室',
                '' + name + '同学,你好！\n'
                            +text+
                            '\n你的个人ID为:' + code+'\n',
                'easyblog123@163.com',
                [mail],
                fail_silently=False
            )
            # send_mail(
            #     '爱特工作室',
            #     '' + name + '同学,你好！\n'
            #                 +text+
            #                 '\n你的个人ID为:' + code+'\n',
            #     'easyblog123@163.com',
            #     [mail],
            #     fail_silently=False
            # )
        except BadHeaderError:
            return HttpResponse('Invalid header found')


def refreshCache():
    from django.core.cache import cache
    cache.clear()


def register(request):
    return render(request, 'apform.html')