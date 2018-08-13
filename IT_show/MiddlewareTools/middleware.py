import re
from MiddlewareTools import mobileDetect
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from user.models import visitUser

class MobileDetectionMiddleware(MiddlewareMixin):
    """
    Useful middleware to detect if the user is
    on a mobile device.
    """
    def process_request(self, request):
        is_mobile = False
        is_tablet = False
        is_phone = False
        user_agent = request.META.get("HTTP_USER_AGENT")
        http_accept = request.META.get("HTTP_ACCEPT")
        if user_agent and http_accept:
            agent = mobileDetect.UAgentInfo(userAgent=user_agent, httpAccept=http_accept)
            is_tablet = agent.detectTierTablet()
            is_phone = agent.detectTierIphone()
            is_mobile = is_tablet or is_phone or agent.detectMobileQuick()
        request.is_mobile = is_mobile
        request.is_tablet = is_tablet
        request.is_phone = is_phone


max_visits = 500 #访问最大次数
min_seconds = 60*10 # 时间段

#只有包含指定信息的访问才被允许
class allowVisit(MiddlewareMixin):
    def process_request(self,request):
        filterIP(request)
        try:
            filterIP(request)
        except Exception as e:
            #if e == 'user ip banned.':
            return HttpResponseForbidden('<h1 style="text-align:center;margin-top:20px;">检测到IP访问次数过多，禁止访问！</h1>')
            #return HttpResponseRedirect("403.html")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        i =1
        pass
    def process_exception(self, request, exception):
        pass

    def process_response(self, request, response):
        return response




def filterIP(request):
    domain = request.META.get('REMOTE_HOST') #获取HOST
    #ip白名单
    white_list = ['googlebot.com', 'crawl.baidu.com', 'sogou.com', 'bing.com', 'yahoo.com']
    #不检查的连接
    request.META.get("url")
    for bot_domain in white_list:
        if domain.find(bot_domain) > 0:
            return bot_domain

    user_ip = request.META['REMOTE_ADDR'] #获取IP

    try:
        record = visitUser.objects.get(ip=user_ip)
    except visitUser.DoesNotExist:
        info = request.META.get("HTTP_USER_AGENT")
        visitUser.objects.create(ip=user_ip, visitNum=1,allNum=1, slotTime=timezone.now(),lastTime=timezone.now(),featureInfo=info)
        return
    # try:
    #     record = visitUser.objects.get(ip=user_ip)
    # except visitUser.DoesNotExist:
    #     visitUser.objects.create(ip=user_ip, visitNum=1, slotTime=timezone.now(),lastTime=timezone.now())
    #     return

    passed_seconds = (timezone.now() - record.slotTime).seconds

    if record.visitNum > max_visits and passed_seconds < min_seconds:#时间段内访问次数太多
        raise Exception('ip is banned')
    else:
        record.lastTime=timezone.now()
        record.allNum = record.allNum + 1

        if passed_seconds < min_seconds:
            record.visitNum = record.visitNum + 1
            record.save()
        else:
            record.visitNum = 1
            record.slotTime =timezone.now()
            record.save()
