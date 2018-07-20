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
import show.views
from django.conf.urls import handler404, handler500
handler404 = "show.views.page404"
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from IT_show.settings import MEDIA_ROOT
import tes.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('base.urls')),
    url(r'^test/', include('tes.urls')),
    url(r'^home/', include('show.urls')),
    url(r'^fresher/', include('user.urls')),
    url('^$', show.views.index, name="index"),
    url(r'^(?P<path>.*)', django.views.static.serve, {'document_root': IT_show.settings.BASE_DIR }),
    # path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
