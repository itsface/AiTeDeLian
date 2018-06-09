from django.shortcuts import render
from django.core.cache import cache
from show.tool import simple_cache_page,refreshCacheThread
from show import models
from django.views.static import serve
from IT_show.settings import MEDIA_ROOT
# Create your views here.

#添加或删除留言时调用该函数
def refreshCache(key):
    newTask=refreshCacheThread(key)
    newTask.start()

#@simple_cache_page(60*60*10,"index")
def index(request):  # success
    return render(request, 'home(pre).html')

#@simple_cache_page(60*60*10,"workshow")
def workshow(request):  # success
    num=models.WorksShow.objects.count()
    web=models.WorksShow.objects.all()
    result={'num':10,'web':web}
    return render(request, 'workshow.html',{'result':result})

#@simple_cache_page(60*60*10,"member")
def member(request):

    m11=models.Member.objects.filter(year=2011)
    m12 = models.Member.objects.filter(year=2012)
    m13=models.Member.objects.filter(year=2013)
    m14 = models.Member.objects.filter(year=2014)
    m15 = models.Member.objects.filter(year=2015)
    m16 = models.Member.objects.filter(year=2016)
    m17 = models.Member.objects.filter(year=2017)
    result = {'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'m16':m16,'m17':m17,'num5':range(1,4),'year':range(2011,2018)}


    return render(request, 'member.html',{'result':result})

#@simple_cache_page(60*60*10,"department")
def department(request):
    qianduan=models.Department.objects.get(name="前端开发")
    chengxu=models.Department.objects.get(name="程序开发")
    ui=models.Department.objects.get(name="UI设计")
    app=models.Department.objects.get(name="APP开发")
    result={"qianduan":qianduan,"chengxu":chengxu,"ui":ui,"app":app}
    return render(request, 'department.html',{'result':result})

#@simple_cache_page(60*60*10,"bigevent")
def big_event(request):
    return render(request, 'bigevent.html')


def comment(request):
    return render(request, 'comment.html');