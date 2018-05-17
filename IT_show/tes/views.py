from django.shortcuts import render
from random import Random
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
from django.views.decorators.cache import cache_page
#这里设置的是 60秒 * 10 ,10分钟
#@cache_page(60 * 10)
def test(request):
    a=(10^10)*(10^10%13)*7%6
    return render(request,"test.html")


def api_comment_submit_test(request):
    return render(request, 'postTest.html')

