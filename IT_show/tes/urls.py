<<<<<<< HEAD
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
urlpatterns = [
    url(r'^page1/', views.test),
=======
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^comment/submit$', api_comment_submit_test, name='api_comment_submit_test'),
>>>>>>> 93b57445b6ff73c03413a39b38c83a32527d01e9
]
