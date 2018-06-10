from django.core.cache import cache
import threading
import time

def simple_cache_page(cache_timeout,keyName):
    """
    Decorator for views that tries getting the page from the cache and
    populates the cache if the page isn't in the cache yet.

    The cache is keyed by view name and arguments.
    """
    def _dec(func):
        def _new_func(*args, **kwargs):
            key = keyName#func.__name__
            if kwargs:
                key += ':' + ':'.join([kwargs[key] for key in kwargs])

            response = cache.get(key)
            if not response:
                response = func(*args, **kwargs)
                cache.set(key, response, cache_timeout)
            return response
        return _new_func
    return _dec

class refreshCacheThread(threading.Thread):
    #prints = tasksThread()
    #prints.start()
    def __init__(self, keyname):
        threading.Thread.__init__(self)
        self.keyname = keyname

    def run(self):
        cache.set(self.keyname, None)
        #response="这里执行函数"
        #cache.set("keyname", response,60*60*10)