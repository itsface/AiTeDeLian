from django.shortcuts import render
from random import Random
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from user.sendMail import send_mail as asynchronousSendEmail
from .form import FresherForm
from show.tool import simple_cache_page,refreshCacheThread
from django.core.mail import send_mail
from user.models import StatusDetails,Fresher
from datetime import datetime, timedelta
from show.models import *
# Create your views here.
import threading
class EmailThread(threading.Thread):
    def __init__(self, name, code, mail,text):
        threading.Thread.__init__(self)
        self.name = name
        self.code = code
        self.mail = mail
        self.text = text

    def run (self):
        send_mail(subject="爱特工作室",from_email="easyblog123@163.com",recipient_list=self.mail,message=self.text)

#异步发邮件
def sendEmail(name, code, mail,text):
        try:
            asynchronousSendEmail(
                '爱特工作室',
                '' + name + '同学,你好！\n'
                            +text+
                            '\n你的个人ID为:' + code+'\n',
                'easyblog123@163.com',
                mail,
                fail_silently=False
             )
        except BadHeaderError:
            return HttpResponse('Invalid header found')

#清除所有缓存
def refreshCache():
    from django.core.cache import cache
    cache.clear()

#@simple_cache_page(60*60*10,"register")
def register(request):
    # from django.db.models import Q
    departments=Department.objects.filter(existing=True)

    return render(request, 'apform.html',{'departments':departments})


#@simple_cache_page(60*60*10,"register")
def registerPhone(request):
    # from django.db.models import Q
    departments=Department.objects.filter(existing=True)

    return render(request, 'apformPhone.html',{'departments':departments})

def addNewStatusDetail(userId,statueId):
    try:
        fresher=Fresher.objects.get(id=userId)
        fresher.status_id = statueId #更新用户状态
        fresher.save()
        if statueId != 0:#将之前的状态置零
            oldStstu=StatusDetails.objects.get(hostID__id=userId, isTail=True)
            oldStstu.isTail=False
            oldStstu.save()

        StatusDetails.objects.create(statu_id=statueId, time=datetime.now(),#添加 新状态信息
                                     hostID_id=userId,
                                     code=StatusDetails.objects.filter(
                                     hostID=fresher.id).count() + 1,isTail=True)
    except:
        pass

