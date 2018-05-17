import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from show.models import Comment, HeadPicture
from user.models import Fresher, StatusDetails
import logging


def api_comment_get(request):
    back = {
        "success": True,
    }
    try:
        oneTimeGet = 10
        code = int(request.GET.get("code", 0))
        if code == 0:
            comments = Comment.objects.all()
        else:
            comments = Comment.objects.filter(code__range=(0, code - 1))
        comments = comments.order_by("-code")
        len = comments.count()
        if len > oneTimeGet:
            len = oneTimeGet
        comments = comments[0:len]
        i = 0
        for c in comments:
            i = i + 1

            back[str(i)] = {
                "head": c.head.pic.url,
                "content": c.content,
                "createTime": c.createTime.strftime("%Y-%m-%d %H:%M:%S"),
                "code": c.code,
            }
    except:
        back["success"] = False
    return HttpResponse(json.dumps(back), content_type="application/json")
    return HttpResponse(json.dumps(back))


def api_comment_get2(request):
    back = []
    try:
        oneTimeGet = 10
        code = int(request.GET.get("code", 0))
        if code == 0:
            comments = Comment.objects.all()
        else:
            comments = Comment.objects.filter(code__range=(0, code - 1))
        comments = comments.order_by("-code")
        len = comments.count()
        if len > oneTimeGet:
            len = oneTimeGet
        comments = comments[0:len]
        i = 0
        for c in comments:
            i = i + 1
            back += [{
                "head": c.head.pic.url,
                "content": c.content,
                "createTime": c.createTime.strftime("%Y-%m-%d %H:%M:%S"),
                "code": c.code,
            }]
    except:
        pass
    return HttpResponse(json.dumps(back))


def api_comment_submit(request):
    back = {
        "success": True,
    }
    try:
        content = request.POST.get("content")
        # logging.debug(content)
        head = int(request.POST.get("head"))
        # logging.debug(content + " " + str(head))
        code = int(Comment.objects.latest("code").code) + 1
        # logging.debug(code)
        c = Comment.objects.create(code=code, content=content, head=HeadPicture.objects.get(id=head))
        c.save()
    except:
        back["success"] = False
    return HttpResponse(json.dumps(back), content_type="application/json")
    return HttpResponse(json.dumps(back))


def api_status_get(request):
    back = []
    try:
        userCode = request.GET.get("userCode", "")
        # logging.debug(userCode)
        statusList = StatusDetails.objects.filter(hostID__userCode=userCode)
        # logging.debug(statusList)
        for status in statusList:
            back += [{
                "statusName": status.statu.info,
                "statusHappenTime": status.time.strftime("%Y-%m-%d %H:%M:%S"),
                "statusOrder": status.code,
            }]
    except:
        pass
    return HttpResponse(json.dumps(back))
