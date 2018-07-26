from django.shortcuts import render
from django.core.cache import cache
from show.tool import simple_cache_page,refreshCacheThread
from django.views.static import serve
from IT_show.settings import MEDIA_ROOT
from show.models import *
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
    result = {
        "num": 0,
        "webSet": None,
    }
    num = WorksShow.objects.count()
    result["num"] = num
    webs = WorksShow.objects.all()
    webSet = {}
    i = 0
    for web in webs:
        webSet[str(i)] = {
            "number": "number" + str(i),
            "name": web.name,
            "link": web.link,
            "pic": web.pic.url,
        }
        i = i + 1
    result["webSet"] = webSet

    return render(request, 'workshow.html', result)

@simple_cache_page(60*60*10,"member")
def member(request):
    result={}
    members=[]
    year=2011
    while year<2018:
        temp = Member.objects.filter(year=year)
        num=int(temp.count()/3)
        if temp.count()%3!=0:
            num=num+1
            print(num)
        temp2={"member":temp,"num":num,"year":year}
        members.append(temp2)
        year=year+1

    result = {'members':members}

    return render(request, 'member.html',{'result':result})

@simple_cache_page(60*60*10,"department")
def department(request):
    qianduan=Department.objects.get(name="前端开发")
    chengxu=Department.objects.get(name="程序开发")
    ui=Department.objects.get(name="UI设计")
    app=Department.objects.get(name="APP开发")
    result=[]
    result.append(qianduan)
    result.append(chengxu)
    result.append(ui)
    result.append(app)

    #result={"qianduan":qianduan,"chengxu":chengxu,"ui":ui,"app":app}
    return render(request, 'department.html',{'result':result})

@simple_cache_page(60*60*10,"bigevent")
def big_event(request):
    num=range(1,9)
    return render(request, 'bigevent.html',{"num":num})


def comment(request):
    result={}
    headImages=HeadPicture.objects.all().order_by("name")
    num=HeadPicture.objects.all().count()
    result={"heads":headImages,"num":num}
    return render(request, 'comment.html',result)

def page404(request):
    return render(request,"404.html")