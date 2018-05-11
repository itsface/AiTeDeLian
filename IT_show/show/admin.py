from django.contrib import admin
from .models import *
from datetime import datetime, timedelta

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'content',"year")
    search_fields = ( 'name', 'content',"year")
    # fields = (
    #     'username',
    #     'password', 'email', 'is_active', 'birthday', 'gender', 'follow_num', 'pub_time', 'address', 'image')
    list_per_page = 10
    #list_filter = ("year")
from django.utils.safestring import mark_safe
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', "year",'intro',"photo","image_tag")
    readonly_fields = ['image_tag']
    search_fields = ( 'name', 'intro',"year")
    list_per_page = 10
    def img_show(self):
        return mark_safe('<img src="%s" height="64" width="64" />' % (self.photo))


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')
    search_fields = ( 'name', 'intro')
    # fields = (
    #     'username',
    #     'password', 'email', 'is_active', 'birthday', 'gender', 'follow_num', 'pub_time', 'address', 'image')
    list_per_page = 10
    #list_filter = (UserFilterSex,UserFilterPubtime,UserFilterStatus)

class WorksShowAdmin(admin.ModelAdmin):
    list_display = ('name','link')
    search_fields = ( 'name','link')
    # fields = (
    #     'username',
    #     'password', 'email', 'is_active', 'birthday', 'gender', 'follow_num', 'pub_time', 'address', 'image')
    list_per_page = 10
    #list_filter = ("year")

admin.site.register(Member,MemberAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Event)
admin.site.register(WorksShow)
admin.site.register(HeadPicture)
admin.site.register(Comment)