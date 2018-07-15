from django.shortcuts import render
from django.core.cache import cache
from show.tool import simple_cache_page,refreshCacheThread
from show import models
from django.views.static import serve
from IT_show.settings import MEDIA_ROOT
# Create your views here.

#添加或删除留言时调用该函数
def refreshCache(key):
    newTask=refreshCacheThread(keyname=key)
    newTask.start()

@simple_cache_page(60*60*10,"index")
def index(request):  # success
    return render(request, 'home.html')

@simple_cache_page(60*60*10,"workshow")
def workshow(request):  # success
    num=models.WorksShow.objects.count()
    web=models.WorksShow.objects.all()
    result={'num':10,'web':web}
    return render(request, 'workshow.html',{'result':result})

@simple_cache_page(60*60*10,"member")
def member(request):

    m11=models.Member.objects.filter(year=2011)
    m12 = models.Member.objects.filter(year=2012)
    m13=models.Member.objects.filter(year=2013)
    m14 = models.Member.objects.filter(year=2014)
    m15 = models.Member.objects.filter(year=2015)
    m16 = models.Member.objects.filter(year=2016)
    m17 = models.Member.objects.filter(year=2017)

    num11 = models.Member.objects.filter(year=2011).count()

    num12 = models.Member.objects.filter(year=2012).count()

    num13 = models.Member.objects.filter(year=2013).count()
    num14 = models.Member.objects.filter(year=2014).count()
    num15 = models.Member.objects.filter(year=2015).count()
    num16 = models.Member.objects.filter(year=2016).count()
    num17 = models.Member.objects.filter(year=2017).count()
    num17=num17 // 3 if num17 % 3 == 0 else num17//3 + 1
    nnum17=range(1,num17+1)
    num11 = range(1,(num11 // 3 if num11 % 3 == 0 else num11//3 + 1)+1)
    num12 = range(1,(num12 // 3 if num12 % 3 == 0 else num12//3 + 1)+1)
    num13 = range(1,(num13 // 3 if num13 % 3 == 0 else num13//3 + 1)+1)
    num14 = range(1,(num14 // 3 if num14 % 3 == 0 else num14//3 + 1)+1)
    num15 = range(1,(num15 // 3 if num15 % 3 == 0 else num15//3 + 1)+1)
    num16 = range(1,(num16 // 3 if num16 % 3 == 0 else num16//3 + 1)+1)
    num17 = range(1,(num17 //  3 if num17 % 3 == 0 else num17//3 + 1)+1)

    result = {'m11':m11,'m12':m12,'m13':m13,'m14':m14,'m15':m15,'m16':m16,'m17':m17,'num5':range(1,4),'year':range(2011,2018),
              'num11':num11,'num12':num12,'num13':num13,'num14':num14,'num15':num15,'num16':num16,'num17':nnum17,
              }

    return render(request, 'member.html',{'result':result})

@simple_cache_page(60*60*10,"department")
def department(request):
    qianduan=models.Department.objects.get(name="前端开发")
    chengxu=models.Department.objects.get(name="程序开发")
    ui=models.Department.objects.get(name="UI设计")
    app=models.Department.objects.get(name="APP开发")
    result={"qianduan":qianduan,"chengxu":chengxu,"ui":ui,"app":app}
    return render(request, 'department.html',{'result':result})

@simple_cache_page(60*60*10,"bigevent")
def big_event(request):
    return render(request, 'bigevent.html')


def comment(request):
    return render(request, 'comment.html');

def page404(request):
    return render(request,"404.html")