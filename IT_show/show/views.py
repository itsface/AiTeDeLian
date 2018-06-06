from django.shortcuts import render
from django.core.cache import cache
from show.tool import simple_cache_page,refreshCacheThread
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
    return render(request, 'workshow.html')

#@simple_cache_page(60*60*10,"member")
def member(request):
    return render(request, 'member.html')

#@simple_cache_page(60*60*10,"department")
def department(request):
    return render(request, 'department.html')

#@simple_cache_page(60*60*10,"bigevent")
def big_event(request):
    return render(request, 'bigevent.html')
