from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', index, name='show_index'),
    url(r'^workshow/$', workshow, name='show_workshow'),
    url(r'^member/$', member, name='show_member'),
    url(r'^department/$', department, name='show_department'),
    url(r'^story/$', big_event, name='show_big_event'),
]
