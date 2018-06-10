from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^new/$', register, name='user_'),

]
