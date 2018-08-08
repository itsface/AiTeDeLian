from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^comment/get$', api_comment_get, name='api_comment_get'),
    url(r'^getComment/(\d+)$', getComment, name='getComment'),
    url(r'^event/get$', api_event_get, name='api_event_get'),
    url(r'^comment/submit$', api_comment_submit, name='api_comment_submit'),
    url(r'^status/get$', api_status_get, name='api_status_get'),
    url(r'^sign/submit$', api_sign_submit, name='api_sign_submit'),
    url(r'^signOK/(?P<code>.*)$', api_sign_ok, name='api_sign_ok'),
    url(r'^identifyPic$', identify_code_picture, name='identify_code_picture'),

    url(r'^workshow/$', getWorkShow, name='getWorkShow'),
    url(r'^member/(\d+)$', getMember, name='getMember'),

    # url(r'^sendInfo/$', sendInfo, name='sendInfo'),
]
