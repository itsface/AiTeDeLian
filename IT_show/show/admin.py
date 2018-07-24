from django.contrib import admin
from .models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from show.tool import refreshCacheThread,simple_cache_page
from xlwt import *
from django.core.cache import cache
from show import forms

def makeExcel(modeladmin, request, queryset):
    # 创建工作簿
    ws = Workbook(encoding='utf-8')
    w = ws.add_sheet(u"爱特成员信息")

    w.write(0, 0, "姓名")
    w.write(0, 1, u"性别")
    w.write(0, 2, u"年份")
    w.write(0, 3, u"部门")
    w.write(0, 4, u"个性签名")

    # 写入内容
    excel_row = 1
    for obj in queryset:
        # data_id = obj.id
        # data_user = obj.username
        # data_time = obj.time.strftime("%Y-%m-%d")[:10]
        # data_content = obj.content
        # dada_source = obj.source
        w.write(excel_row, 0, obj.name)
        w.write(excel_row, 1, "女" if obj.sex else "男")
        w.write(excel_row, 2, obj.year)
        w.write(excel_row, 3, str(obj.department))
        w.write(excel_row, 4, obj.intro)
        excel_row += 1
    # 检测文件是够存在
    # 方框中代码是保存本地文件使用，如不需要请删除该代码
    ###########################
    import os
    fileName = "menbersInfo.xls"
    exist_file = os.path.exists(fileName)
    if exist_file:
        os.remove(fileName)
    ws.save(fileName)
    ############################
    from io import StringIO, BytesIO
    sio = BytesIO()
    ws.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + fileName  # test.xls'
    response.write(sio.getvalue())
    return response


makeExcel.short_description = "导出所选用户信息为excel"


class EventFilterTime(admin.SimpleListFilter):
    title = u'时间'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            (datetime.now().year, str(datetime.now().year) + "年"),
            (datetime.now().year - 1, str(datetime.now().year - 1) + "年"),
            (datetime.now().year - 2, str(datetime.now().year - 2) + "年"),
            ('0', u'更久前'),
        )

    def queryset(self, request, queryset):
        if self.value() != None:
            if self.value() == "0":
                return queryset.filter(year__lte=int(int(self.value()) - 3))
            return queryset.filter(year=self.value())


class UserFilterSex(admin.SimpleListFilter):
    title = u'性别'
    parameter_name = 'sex'

    def lookups(self, request, model_admin):
        return (
            ('0', u'男'),
            ('1', u'女')
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(sex=0)
        elif self.value() == '1':
            return queryset.filter(sex=1)


class UserFilterDepartment(admin.SimpleListFilter):
    title = u'部门'
    parameter_name = 'department'

    def lookups(self, request, model_admin):
        result = []
        import show.models
        for info in show.models.Department.objects.all():
            t = (info.id, info.name)
            result.append(t)
        return result

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(department=self.value())

class UserFilterYear(admin.SimpleListFilter):
    title = u'时间'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            (datetime.now().year, str(datetime.now().year) + "年"),
            (datetime.now().year - 1, str(datetime.now().year - 1) + "年"),
            (datetime.now().year - 2, str(datetime.now().year - 2) + "年"),
            (datetime.now().year - 3, str(datetime.now().year - 3) + "年"),
            (datetime.now().year - 4, str(datetime.now().year - 4) + "年"),
            ('0', u'更久前'),
        )

    def queryset(self, request, queryset):
        if self.value() != None:
            if self.value() == "0":
                return queryset.filter(year__lte=int(int(self.value()) - 3))
            return queryset.filter(year=self.value())


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', "year")
    search_fields = ('name', 'content', "year")
    # fields = (
    #     'username',
    #     'password', 'email', 'is_active', 'birthday', 'gender', 'follow_num', 'pub_time', 'address', 'image')
    list_per_page = 10
    # list_filter = ("year")


from django.utils.safestring import mark_safe


class MemberAdmin(admin.ModelAdmin):

    list_display = ('name', "sex", "year", "department", 'intro', "photo", "image_tag")
    readonly_fields = ['image_tag',"fullImage"]
    search_fields = ('name', 'intro', "year", "sex", "department")
    fields = ('name', "sex", "year", "department", 'intro', "photo", "fullImage")
    #raw_id_fields = ("department",)
    list_per_page = 10
    list_filter = (UserFilterSex, UserFilterDepartment,UserFilterYear)
    actions = [makeExcel]
    form = forms.MenberForm
    def save_model(self, request, obj, form, change):
        obj.save()

        cache.set('member', None, 0)

    def delete_model(self, request, obj):
        obj.delete()
        cache.set('member', None, 0)








class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro',"pic", "image_tag")
    search_fields = ('name', 'intro')
    fields = ('name', 'intro',"pic", "image_tag")
    readonly_fields = ["image_tag"]
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.save()
        cache.set('department', None, 0)

    def delete_model(self, request, obj):
        obj.delete()
        cache.set('department', None, 0)


class WorksShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name', 'link')
    # fields = (
    #     'username',
    #     'password', 'email', 'is_active', 'birthday', 'gender', 'follow_num', 'pub_time', 'address', 'image')
    list_per_page = 10
    # list_filter = ("year")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('code',"name", "image_tag", 'content', "reply","createTime")
    fields = ('code',"name","createTime", 'content', "reply", "image_tag","head")
    readonly_fields = ("createTime","image_tag","code")
    search_fields = ('code', 'content',"name",)
    list_per_page = 30


class HeadPictureAdmin(admin.ModelAdmin):
    list_display = ('name', "image_tag", 'pic')
    fields = ('name', "image_tag", 'pic')
    search_fields = ('name', 'pic')
    readonly_fields = ["name","image_tag"]
    list_per_page = 30



class worksShowAdmin(admin.ModelAdmin):
    list_display = ('name', "image_tag", "link", 'pic')
    fields = ('name', "link", 'pic', "image_tag")
    readonly_fields = ["image_tag"]
    search_fields = ('name', "link")
    list_per_page = 30
    def save_model(self, request, obj, form, change):
        obj.save()
        cache.set('workshow', None, 0)

    def delete_model(self, request, obj):
        obj.delete()
        cache.set('workshow', None, 0)


class eventAdmin(admin.ModelAdmin):
    list_display = ('name', "content", 'year')
    search_fields = ('name', "content", "year")
    list_per_page = 30
    fields = ('name',  "content", 'year')
    form = forms.EventForm


    list_filter = (EventFilterTime,)

    def save_model(self, request, obj, form, change):
        obj.save()
        cache.set('bigevent', None, 0)

    def delete_model(self, request, obj):
        obj.delete()
        cache.set('bigevent', None, 0)

admin.site.site_header = '爱特展示网后台管理'
admin.site.site_title = '后台管理'
admin.site.index_title = '爱特展示网'
admin.site.register(Member, MemberAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Event, eventAdmin)
admin.site.register(WorksShow, worksShowAdmin)
admin.site.register(HeadPicture, HeadPictureAdmin)
admin.site.register(Comment, CommentAdmin)
