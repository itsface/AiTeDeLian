from django.shortcuts import render
from random import Random
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from user.sendMail import send_mail as asynchronousSendEmail
from .form import FresherForm
from show.tool import simple_cache_page,refreshCacheThread
# Create your views here.

#异步发邮件
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

#清除所有缓存
def refreshCache():
    from django.core.cache import cache
    cache.clear()

#@simple_cache_page(60*60*10,"register")
def register(request):
    return render(request, 'apform.html')