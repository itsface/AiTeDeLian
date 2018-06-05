import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from show.models import Comment, HeadPicture
from user.models import Fresher, StatusDetails
from .func import *
import logging
from django.core.mail import send_mail, BadHeaderError
from PIL import Image, ImageDraw, ImageFont, ImageFilter


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
    response = HttpResponse(json.dumps(back), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response
    #return HttpResponse(json.dumps(back), content_type="application/json")


def api_status_get(request):
    back = {
        "success": True,
        "status": [],
    }
    try:
        userCode = request.GET["userCode"]
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
    response = HttpResponse(json.dumps(back), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response
    #return HttpResponse(json.dumps(back), content_type="application/json")


def api_comment_submit(request):
    back = {
        "statusCode": 1,  # 未知错误
    }
    try:
        content = request.POST.get("content")
        # logging.debug(content)
        head = int(request.POST.get("head"))
        # logging.debug(content + " " + str(head))
        code = int(Comment.objects.latest("code").code) + 1
        # logging.debug(code)
        identify = str(request.POST['identify'])
        if identify.upper() != str(request.session['identify']).upper():
            back["statusCode"] = 2  # u"验证码错误"
            raise RuntimeError()
        try:
            del request.session['identify']
        except:
            pass
        c = Comment.objects.create(code=code, content=content, head=HeadPicture.objects.get(id=head))
        c.save()
        back["statusCode"] = 0  # 成功
    except:
        pass
    response = HttpResponse(json.dumps(back), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response
    #return HttpResponse(json.dumps(back), content_type="application/json")
    # return HttpResponse(json.dumps(back))


def api_sign_submit(request):
    back = {
        "statusCode": 1,  # 未知错误
    }
    try:
        back["message"] = "表单获取错误"
        name = request.POST.get("name")  # nchar
        sex = request.POST.get("sex")  # bool
        yearAndMajor = request.POST.get("yearAndMajor")  # nchar
        email = request.POST.get("email")  # email
        phone = request.POST.get("phone")  # nchar
        selfIntro = request.POST.get("selfIntro")  # text
        wantDepartment = request.POST.get("wantDepartment")  # int

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
                + '你的个人ID为:' + code + '\n'
                + '使用该ID能在查询页查询招新状态，也用于完成注册\n'
                + '最后一步，复制以下链接到地址栏并转到完成报名\n'
                + '127.0.0.1:8000/api/signOK/' + code,  # 上线的时候千万记得改这个东西
                'easyblog123@163.com',
                [email],
                fail_silently=False
            )
        except BadHeaderError:
            back["statusCode"] = 2  # 邮件错误
            logging.debug("邮件错了")
            raise RuntimeError()

        newFresher = Fresher.objects.create(name=name, sex=sex, yearAndMajor=yearAndMajor,
                                            email=email, phone=phone, selfIntro=selfIntro,
                                            status_id=1, wantDepartment_id=wantDepartment,
                                            userCode=code)
        logging.debug(newFresher)
        request.session[code] = newFresher.id
        newFresher.save()
        back["statusCode"] = 0  # 成功
    except:
        pass
    logging.debug(back["message"])
    response = HttpResponse(json.dumps(back), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response
    #return HttpResponse(json.dumps(back), content_type="application/json")


def api_sign_ok(request, code):
    try:
        newFresherId = request.session[code]
        newFresher = Fresher.objects.get(id=newFresherId)
        newFresher.active = True
        newFresher.save()
        try:
            del request.session[code]
        except:
            pass
        return HttpResponse("注册成功")
    except:
        return HttpResponse("出现错误，注册失败")


def identify_code_picture(request):
    width, height = identifySize
    image = Image.new('RGBA', (width, height), identifyBgcolor)
    font = ImageFont.truetype("arial", size=25)
    draw = ImageDraw.Draw(image)
    text = randomString(chNum + chAlphaHigh + chAlphaLow, identifyLen)
    draw.text((1, 1),
              text,
              font=font,
              fill=identifyFontcolor)
    if identifyDraw_line:
        for i in range(0, random.randint(1, identifyLine_number)):
            begin = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0, width), random.randint(0, height))
            draw.line([begin, end], fill=identifyLinecolor)
    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
    request.session['identify'] = text
    try:
        image.save(identifyPath)
    except:
        try:
            image.save(identifyPath, "PNG")
        except:
            os.makedirs(identifyDir)
            image.save(identifyPath, "PNG")
    image = open(identifyPath, "rb").read()
    return HttpResponse(image, content_type="image/png")
