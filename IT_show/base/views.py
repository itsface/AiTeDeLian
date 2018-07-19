import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from show.models import Comment, HeadPicture,Event
from user.models import Fresher, StatusDetails,StatusInfo
from .func import *
import logging
from django.core.mail import send_mail, BadHeaderError
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from user.views import sendEmail
from user.views import addNewStatusDetail

from show.tool import simple_cache_page

#@simple_cache_page(60*60*6,"comment")
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
                "nickname": c.name,
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

def getComment(request,code):
    back = {
        "success": True,
        "comment": [],
    }
    try:
        oneTimeGet = 10
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
                "nickname": c.name,
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
    # return HttpResponse(json.dumps(back), content_type="application/json")

def api_status_get(request):
    back = {
        "success": True,
        "name": "",
        "major": "",
        "wantDepart": "",
        "status": [],
    }
    try:
        userCode = request.GET["userCode"]
        # logging.debug(userCode)
        user = Fresher.objects.get(userCode=userCode)
        back["name"] = user.name
        back["major"] = user.yearAndMajor
        back["wantDepart"] = user.wantDepartment.name

        statusList = StatusDetails.objects.filter(hostID__userCode=userCode).order_by("-time")
        # logging.debug(statusList)
        for status in statusList[0:3]:
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
        "statusC": 1,  # 未知错误
    }
    try:
        content = request.POST.get("content")
        # logging.debug(content)
        if len(content) <= 80:
            head = int(request.POST.get("head"))
            # logging.debug(content + " " + str(head))
            code = int(Comment.objects.latest("code").code) + 1
            # logging.debug(code)
            nickName = request.POST.get("nickName")
            logging.debug(nickName)
            identify = str(request.POST['identify'])
            if identify.upper() != str(request.session['identify']).upper():
                back["statusC"] = 2  # u"验证码错误"
                raise RuntimeError()
            try:
                del request.session['identify']
            except:
                pass
            c = Comment.objects.create(code=code, content=content, head=HeadPicture.objects.get(name=head), name=nickName)
            c.save()
            back["statusC"] = 0  # 成功
            from show.views import refreshCache
            refreshCache("comment")
        else:
            back["statusC"] = 1
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

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_sign_submit(request):
    back = {
        "statusC": 1,  # 未知错误
    }
    try:
        back["statusC"] = 3  # "表单获取错误"
        name = request.POST.get("name")  # nchar
        # sex = request.POST.get("sex")  # bool
        yearAndMajor = request.POST.get("yearAndMajor")  # nchar
        email = request.POST.get("email")  # email
        qqnum = request.POST.get("qq")  # nchar
        phone = request.POST.get("phone")  # nchar
        selfIntro = request.POST.get("selfIntro")  # text
        wantDepartment = int(request.POST.get("wantDepartment"))  # int

        #判断邮箱注册次数
        if Fresher.objects.filter(email=email).count() <= 2:
            logging.debug(name)
            # logging.debug(sex)
            logging.debug(yearAndMajor)
            logging.debug(qqnum)
            logging.debug(email)
            logging.debug(phone)
            logging.debug(selfIntro)
            logging.debug(wantDepartment)

            code = randomCode()
            logging.debug(code)
            back["statusC"] = 4  # "邮件发送错误"
            # try:
            #     text="你的报名信息已经收到，请复制以下链接到地址栏并转到完成报名\n http://222.195.145.152:2018/api/signOK/"+code
            # #     + '127.0.0.1:8000/api/signOK/'"
            #     sendEmail(name=name,code=code,mail=email,text=text)
            # except :
            #     logging.debug("邮件错了")
            #     raise RuntimeError()

            back["statusC"] = 2  # 数据库错误
            newFresher = Fresher.objects.create(name=name,  # sex=sex,
                                                yearAndMajor=yearAndMajor,
                                                email=email, qqnum=qqnum, phone=phone,
                                                selfIntro=selfIntro, status_id=0,
                                                wantDepartment_id=wantDepartment,
                                                userCode=code)
            # addNewStatusDetail(newFresher.id,0)
            logging.debug(newFresher)
            request.session[code] = newFresher.id
            newFresher.save()
            back["statusC"] = 0  # 成功
        else:
            back["statusC"] = 5 #邮箱超过最大使用次数3次
    except:
        pass
    logging.debug(back["statusC"])
    response = HttpResponse(json.dumps(back), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response
    #return HttpResponse(json.dumps(back), content_type="application/json")


def api_sign_ok(request, code):
    # try:
        # newFresherId = request.session[code]
        newFresher=Fresher.objects.get(userCode=code)
        # newFresher = Fresher.objects.get(id=newFresherId)
        if newFresher.active==True:
            return HttpResponse("该账号已被激活，链接失效")
        newFresher.active = True
        newFresher.save()

        statuId=newFresher.status_id
        newId=StatusInfo.objects.get(code=statuId).nextStatus_id
        addNewStatusDetail(newFresher.id,newId)



        text = "激活成功，你的报名信息正在等待审核"
        #     + '127.0.0.1:8000/api/signOK/'"
        sendEmail(name=newFresher.name, code=code, mail=newFresher.email, text=text)


        try:
            del request.session[code]
        except:
            pass

        return HttpResponse("激活成功")
    # except:
    #     return HttpResponse("链接已失效，请重新报名。")

def api_event_get(request):
    result = {
        "success": True,
        "events": [],
    }
    try:
        year=request.GET.get("year")
        events=Event.objects.filter(year=year)
        result["success"]=True
        for event in events:
            temp={"name":event.name,"content":event.content}
            result["events"].append(temp)
    except:
        result["success"] = False
    response = HttpResponse(json.dumps(result), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response

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
