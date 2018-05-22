import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from show.models import Comment, HeadPicture
from user.models import Fresher, StatusDetails
from .func import randomCode
import logging
from django.core.mail import send_mail, BadHeaderError


def api_comment_get(request):
    back = {
        "success": True,
        "comment": [],
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
            back["comment"] += [{
                "head": c.head.pic.url,
                "content": c.content,
                "createTime": c.createTime.strftime("%Y-%m-%d %H:%M:%S"),
                "code": c.code,
            }]
    except:
        back["success"] = False
    return HttpResponse(json.dumps(back), content_type="application/json")


def api_status_get(request):
    back = {
        "success": True,
        "status": [],
    }
    try:
        userCode = request.GET.get("userCode", "")
        # logging.debug(userCode)
        statusList = StatusDetails.objects.filter(hostID__userCode=userCode)
        # logging.debug(statusList)
        for status in statusList:
            back["status"] += [{
                "statusName": status.statu.info,
                "statusHappenTime": status.time.strftime("%Y-%m-%d %H:%M:%S"),
                "statusOrder": status.code,
            }]
    except:
        back["success"] = False
    return HttpResponse(json.dumps(back), content_type="application/json")


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
    # return HttpResponse(json.dumps(back))


def api_sign_submit(request):
    back = {
        "success": False,
        "message": "未知错误",
    }
    try:
        back["message"] = "表单获取错误"
        name = request.POST.get("name")                              # nchar
        sex = request.POST.get("sex")                                # bool
        yearAndMajor = request.POST.get("yearAndMajor")              # nchar
        email = request.POST.get("email")                            # email
        phone = request.POST.get("phone")                            # nchar
        selfIntro = request.POST.get("selfIntro")                    # text
        wantDepartment = request.POST.get("wantDepartment")          # int

        logging.debug(name)
        logging.debug(sex)
        logging.debug(yearAndMajor)
        logging.debug(email)
        logging.debug(phone)
        logging.debug(selfIntro)
        logging.debug(wantDepartment)

        code = randomCode()
        back["message"] = "邮件发送错误"
        try:
            send_mail(
                '爱特工作室',
                ''
                + name + '同学,你好！\n'
                + '你已成功报名爱特招新'
                + '你的个人ID为:' + code+'\n'
                + '使用该ID能在查询页查询招新状态',
                'easyblog123@163.com',
                [email],
                fail_silently=False
            )
        except BadHeaderError:
            logging.debug("邮件错了")

        back["message"] = "数据库错误"
        newFresher = Fresher.objects.create(name=name, sex=sex, yearAndMajor=yearAndMajor,
                                            email=email, phone=phone, selfIntro=selfIntro,
                                            status_id=1, wantDepartment_id=wantDepartment,
                                            userCode=code)
        logging.debug(newFresher)
        newFresher.save()
        back["success"] = True
        back["message"] = "成功"
    except:
        pass
    logging.debug(back["message"])
    return HttpResponse(json.dumps(back), content_type="application/json")