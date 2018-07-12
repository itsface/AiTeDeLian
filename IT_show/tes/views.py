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
@simple_cache_page(keyName="test",cache_timeout=60 * 10)
def test(request):
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