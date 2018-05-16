from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^comment/submit$', api_comment_submit_test, name='api_comment_submit_test'),
]
