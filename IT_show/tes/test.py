
##通过thread 实现django中
import threading
import time
import os,django
import flag
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IT_show.settings")
import base.views
#name, code, mail,text
base.views.sendEmail("tuotuo","asd",["983739298@qq.com"],"hello,world")
