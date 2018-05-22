from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^comment/get$', api_comment_get, name='api_comment_get'),
    url(r'^comment/submit$', api_comment_submit, name='api_comment_submit'),
    url(r'^status/get$', api_status_get, name='api_status_get'),
    url(r'^sign/submit$', api_sign_submit, name='api_sign_submit'),
]
