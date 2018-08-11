from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', index, name='show_index'),
    url(r'^indexM/$', indexM, name='show_indexM'),


    url(r'^workshow/$', workshow, name='show_workshow'),
    url(r'^workshowM/$', workshowM, name='show_workshowM'),

    url(r'^member/$', member, name='show_member'),


    url(r'^department/$', department, name='show_department'),
    url(r'^departmentM/$', departmentM, name='show_departmentM'),

    url(r'^story/$', big_event, name='show_big_event'),
    url(r'^comment/$', comment, name='show_comment'),

]
