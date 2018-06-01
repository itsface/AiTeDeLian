
"""IT_show URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import django.views.static
import IT_show.settings
from . import views
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^page1/(?P<slug>.+)$', simple_cache_page(60 * 60 * 24)(views.test), name='page1'),
    url(r'^page2/(?P<slug>.+)$', simple_cache_page(60 * 60 * 24)(views.test2), name='page2'),
    url(r'^comment/submit$', api_comment_submit_test, name='api_comment_submit_test'),
    url(r'^sign/submit$', api_sign_submit_test, name='api_sign_submit_test'),

]
