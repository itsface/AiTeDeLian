from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import threading
import time
# Create your views here.


def simple_cache_page(cache_timeout,keyName):
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


class tasksThread(threading.Thread):
    #prints = tasksThread()
    #prints.start()
    def run(self):
        print("start.... %s" % (self.getName(),))
        for i in range(5):
            time.sleep(1)
            print("start.... %s" % (self.getName(),))