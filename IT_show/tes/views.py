from django.shortcuts import render
from random import Random
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import json


#清除所有缓存
def test4(request):
    from django.core.cache import cache
    cache.clear()
    return HttpResponse("清除完毕")

def test3(request):
    from IT_show import settings
    if settings.isNew:
        print("new")
        settings.isNew=False
    else:
        print("old")
        settings.isNew=True
    return render(request, "test.html",{"isNew":settings.isNew})

#页面缓存装饰器
def simple_cache_page(keyName,cache_timeout):
    """
    Decorator for views that tries getting the page from the cache and
    populates the cache if the page isn't in the cache yet.

    The cache is keyed by view name and arguments.
    """
    def _dec(func):
        def _new_func(*args, **kwargs):
            key = func.__name__
            if kwargs:
                key += ':' + ':'.join([kwargs[key] for key in kwargs])

            response = cache.get(key)
            if not response:
                response = func(*args, **kwargs)
                cache.set(key, response, cache_timeout)
            return response
        return _new_func
    return _dec

#这里设置的是 60秒 * 10 ,10分钟
def test(request):
    # def checkMobile(request):
    #     """
    #     demo :
    #         @app.route('/m')
    #         def is_from_mobile():
    #             if checkMobile(request):
    #                 return 'mobile'
    #             else:
    #                 return 'pc'
    #     :param request:
    #     :return:
    #     """
    #     userAgent = request.headers['User-Agent']
    #     # userAgent = env.get('HTTP_USER_AGENT')
    #
    #     _long_matches = r'googlebot-mobile|android|avantgo|blackberry|blazer|elaine|hiptop|ip(hone|od)|kindle|midp|mmp|mobile|o2|opera mini|palm( os)?|pda|plucker|pocket|psp|smartphone|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce; (iemobile|ppc)|xiino|maemo|fennec'
    #     _long_matches = re.compile(_long_matches, re.IGNORECASE)
    #     _short_matches = r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-'
    #     _short_matches = re.compile(_short_matches, re.IGNORECASE)
    #
    #     if _long_matches.search(userAgent) != None:
    #         return True
    #     user_agent = userAgent[0:4]
    #     if _short_matches.search(user_agent) != None:
    #         return True
    #     return False

    temp=""
    if request.is_phone:
        temp+="phone  "
    if request.is_mobile:
        temp+="mobile  "
    if request.is_tablet:
        temp += "tablet  "
    return render(request, "test.html",{"temp":temp})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def postTest(request):
    back={"success":True}
    if request.method=="POST":
        text=request.POST.get("text")
        back["text"]="您老传的内容是："+text
        print(text)
    else:
        back = {"success": False}
    response = HttpResponse(json.dumps(back), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response
    return render(request, "test.html")

def test2(request):
    cache.set("test", None,0*0)
    return render(request, "test.html")

def setCache():
    from django.core.cache import cache
    key="缓存内容"
    time=60*10
    result=cache.get(key)
    if not result:
        result=""
        cache.set(key,result,time)
    return result

from user.models import *
def sendEmailTest(request):
    pass
    users=Fresher.objects.filter()


from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
def expire_page(path):
    request = HttpRequest()
    request.path = path
    key = get_cache_key(request)
    if cache.has_key(key):
        cache.delete(key)



def invalidate_cache(path=''):
    ''' this function uses Django's caching function get_cache_key(). Since 1.7,
        Django has used more variables from the request object (scheme, host,
        path, and query string) in order to create the MD5 hashed part of the
        cache_key. Additionally, Django will use your server's timezone and
        language as properties as well. If internationalization is important to
        your application, you will most likely need to adapt this function to
        handle that appropriately.
    '''
    from django.core.cache import cache
    from django.http import HttpRequest
    from django.utils.cache import get_cache_key

    # Bootstrap request:
    #   request.path should point to the view endpoint you want to invalidate
    #   request.META must include the correct SERVER_NAME and SERVER_PORT as django uses these in order
    #   to build a MD5 hashed value for the cache_key. Similarly, we need to artificially set the
    #   language code on the request to 'en-us' to match the initial creation of the cache_key.
    #   YMMV regarding the language code.
    request = HttpRequest()
    request.META = {'SERVER_NAME':'localhost','SERVER_PORT':8000}
    request.LANGUAGE_CODE = 'en-us'
    request.path = path

    try:
        cache_key = get_cache_key(request)
        if cache_key :
            if cache.has_key(cache_key):
                cache.delete(cache_key)
                return (True, 'successfully invalidated')
            else:
                return (False, 'cache_key does not exist in cache')
        else:
            raise ValueError('failed to create cache_key')
    except (ValueError, Exception) as e:
        return (False, e)




def api_comment_submit_test(request):
    return render(request, 'postTest.html')

def api_sign_submit_test(request):
    return render(request, 'postTest2.html')

#下面的测试代码
from django.middleware.cache import CacheMiddleware
from django.utils.decorators import decorator_from_middleware_with_args

def extended_cache_page(cache_timeout, key_prefix=None, cache=None):
    return decorator_from_middleware_with_args(ExtendedCacheMiddleware)(
        cache_timeout=cache_timeout,
        cache_alias=cache,
        key_prefix=key_prefix,
    )

class ExtendedCacheMiddleware(CacheMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if callable(self.key_prefix):
            self.key_function = self.key_prefix

    def key_function(self, request, *args, **kwargs):
        return self.key_prefix

    def get_key_prefix(self, request):
        return self.key_function(
            request,
            *request.resolver_match.args,
            **request.resolver_match.kwargs
        )

    def process_request(self, request):
        self.key_prefix = self.get_key_prefix(request)
        return super().process_request(request)

    def process_response(self, request, response):
        self.key_prefix = self.get_key_prefix(request)
        return super().process_response(request, response)

from django.utils.lru_cache import lru_cache

@lru_cache()
def last_modified(request, blog_id):
    return blog_id

# @extended_cache_page(60 * 15, key_prefix=last_modified)
# def test(request, blog_id):
#         return render(request, "test.html")