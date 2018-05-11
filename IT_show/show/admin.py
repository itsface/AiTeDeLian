from django.contrib import admin
from .models import *
from datetime import datetime, timedelta

class EventFilterTime(admin.SimpleListFilter):
    title = u'时间'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            (datetime.now().year, str(datetime.now().year)+"年"),
            (datetime.now().year-1, str(datetime.now().year-1)+"年"),
            (datetime.now().year-2, str(datetime.now().year-2)+"年"),
            ('0', u'更久前'),
        )

    def queryset(self, request, queryset):
        if self.value()!=None:
            if self.value()=="0":
                return queryset.filter(year__lte=int(int(self.value())-3))
            return queryset.filter(year=self.value())


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
    fields=('name', "year",'intro',"photo","image_tag")
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.save()


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro',"image_tag")
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

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',"image_tag",'content',"createTime")
    search_fields = ( 'name','content')
    list_per_page = 30

class HeadPictureAdmin(admin.ModelAdmin):
    list_display = ('name',"image_tag",'pic')
    search_fields = ( 'name','pic')
    list_per_page = 30

class worksShowAdmin(admin.ModelAdmin):
    list_display = ('name',"image_tag","link",'pic')
    search_fields = ( 'name',"link")
    list_per_page = 30

class eventAdmin(admin.ModelAdmin):
    list_display = ('name',"image_tag","content",'year',"pic")
    search_fields = ( 'name',"content","year")
    list_per_page = 30

    list_filter = (EventFilterTime,)

admin.site.register(Member,MemberAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Event,eventAdmin)
admin.site.register(WorksShow,worksShowAdmin)
admin.site.register(HeadPicture,HeadPictureAdmin)
admin.site.register(Comment,CommentAdmin)