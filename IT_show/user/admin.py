from django.contrib import admin
from .models import *
from datetime import datetime, timedelta
import user.views
import show.models
import user.models
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin, messages
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from user import models
from xlwt import *
from django import forms
from django.views.decorators.csrf import csrf_exempt
import logging
from show import forms as checkForm

# Register your models here.
# class CaseAdmin(admin.ModelAdmin):
#     # form = CaseForm
#     actions = ['update_data_src']
#
#     class data_src_form(forms.forms.Form):
#         _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
#         data_src = forms.ModelChoiceField(user.models.Fresher.objects)

# action函数

def SetNewStatusDetails(userId, statuId : -1):
    try:
        user = Fresher.objects.get(id=userId)
    except:
        return False

    if statuId == -1:
        try:
            statuId = user.status.nextStatus_id
        except:
            return False
    try:
        statu = StatusInfo.objects.get(code=statuId)
    except:
        return False

    code = 1
    tailDetail = None
    try:
        tailDetail = StatusDetails.objects.get(hostID=user, isTail=True)
        code = tailDetail.code + 1
        logging.debug(code)
    except:
        pass

    try:
        newDetail = StatusDetails.objects.create(code=code, hostID=user, statu=statu)
        try:
            tailDetail.isTail = False
            tailDetail.save()
        except:
            pass
        newDetail.save()
    except:
        return False
    logging.debug("新链生成成功")
    return True

def setNewStatues(userId):
    try:
        oldDetail = models.StatusDetails.objects.get(hostID=userId, isTail=1)
    except:
        oldDetail = None
    if oldDetail != None:
        oldDetail.isTail = False
        oldDetail.save()


def DeleteStatusDetails(userId):
    try:
        tailDetail = StatusDetails.objects.get(hostID__id=userId, isTail=True)
        code = tailDetail.code - 1
        # logging.debug(code)
        if code == 0:
            return False
        tailDetail.delete()
        tailDetail = StatusDetails.objects.get(hostID__id=userId, code=code)
        tailDetail.isTail = True
        tailDetail.save()
    except:
        return False


def update_data_src(modeladmin, request, queryset):
    form = None
    if 'cancel' in request.POST:
        modeladmin.message_user(request, u'已取消操作')
        return
    elif 'data_src' in request.POST:
        form = modeladmin.data_src_form(request.POST)
        if form.is_valid():
            ok = 0
            fail = 0
            data_src = form.cleaned_data['data_src']
            for case in queryset:
                try:
                    if case.active == False:
                        messages.warning(request, u"用户" + case.name + "未激活，请先执行激活操作")
                        continue
                    case.status_id = data_src.code
                    case.save()
                    if case.status_id != None and case.status.emailText != "":
                        user.views.sendEmail(case.name, case.userCode, case.email,
                                             models.StatusInfo.objects.get(code=data_src.code).emailText)
                    if case.status != None:
                        setNewStatues(case.id)
                        newInfo = user.models.StatusDetails.objects.create(statu_id=case.status.code, time=datetime.now(),
                                                                           hostID_id=case.id,
                                                                           code=user.models.StatusDetails.objects.filter(
                                                                               hostID=case.id).count() + 1)
                    ok=ok+1
                except:
                    fail=fail+1
                    msg = str(fail) + ".用户" + case.name + "的状态修改失败."
                    messages.add_message(request, messages.ERROR, msg)
            if ok > 0:
                msg = "已成功改变" + str(ok) + "名用户的状态."
                modeladmin.message_user(request, msg)
            if fail > 0:
                msg = str(fail) + "名用户的状态改变失败."
                messages.add_message(request, messages.ERROR, msg)
            return HttpResponseRedirect(request.get_full_path())
        else:
            messages.warning(request, u"请选择数据源")
            form = None

    if not form:
        form = modeladmin.data_src_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

    return render(request, 'batch_update.html',
                  {'objs': queryset, 'form': form, 'path': request.get_full_path(),
                   'action': 'update_data_src', 'title': u'将所选用户跳转至如下状态'},
                  )

update_data_src.short_description = u'将所选用户跳转至指定状态，并发送邮件通知'


def sendStatuInfo(modeladmin, request, queryset):
    ok1=0
    ok2=0
    fail=0
    for fresher in queryset:
        try:
            if  fresher.status_id!=None and fresher.status.emailText!="":
                text = fresher.status.emailText
                if fresher.active == False:
                    from IT_show.settings import localHost
                    text = text + "\n激活链接：" + str(localHost) + "/api/signOK/" + fresher.userCode

                user.views.sendEmail(fresher.name, fresher.userCode, fresher.email, text)
                ok1=ok1+1
            else:
                ok2=ok2+1
                messages.warning(request, u"用户" + fresher.name + "当前状态无邮件内容")

        except:
            fail=fail+1
            msg = str(fail) + ".用户" + fresher.name + "的邮件通知发送失败."
            messages.add_message(request, messages.ERROR, msg)
    if ok1>0:
        modeladmin.message_user(request, str(ok1)+"名用户邮件通知发送完成.")
    if ok2 > 0:
        messages.warning(request, str(ok2) + "名用户当前状态无邮件内容.")
    if fail > 0:
        msg = str(fail) + "名用户邮件通知发送失败."
        messages.add_message(request, messages.ERROR, msg)

sendStatuInfo.short_description = "给所选用户发送当前状态通知"


def statusToNext(modeladmin, request, queryset):
    ok = 0
    fail = 0
    for fresher in queryset:
        try:
            try:
                if fresher.active==False:
                    messages.warning(request, u"用户"+fresher.name+"未激活，请先执行激活操作")
                    continue
                newStatusId = models.StatusInfo.objects.get(code=fresher.status.code).nextStatus_id
            except:
                newStatusId = None
            if newStatusId:
                fresher.status__code=newStatusId
                fresher.status_id = newStatusId
                #SetNewStatusDetails(fresher.id, newStatusId)
                fresher.save()
                setNewStatues(fresher.id)
                if fresher.status_id != None and fresher.status.emailText != "":
                    user.views.sendEmail(fresher.name, fresher.userCode, fresher.email, models.StatusInfo.objects.get(code=newStatusId).emailText)
                if fresher.status != None:
                    newInfo = user.models.StatusDetails.objects.create(statu_id=fresher.status_id, time=datetime.now(),
                                                                       hostID_id=fresher.id,code=user.models.StatusDetails.objects.filter(hostID=fresher.id).count()+1)
                ok=ok+1
            else:
                messages.warning(request, u"用户" + fresher.name + "的状态已到达链顶端")
        except:
            fail=fail+1
            msg = str(fail) + ".用户"+fresher.name+"的状态改变失败."
            messages.add_message(request, messages.ERROR, msg)
    if ok > 0:
        msg = "已成功改变"+str(ok) + "名用户的状态."
        modeladmin.message_user(request,msg )
    if fail > 0:
        msg = str(fail) + "名用户的状态改变失败."
        messages.add_message(request, messages.ERROR, msg)

statusToNext.short_description = "所选用户跳转至下一状态，并发送邮件通知"

def takeToInfoList(modeladmin, request, queryset):
    ok1=0
    ok2=0
    fail=0
    for fresher in queryset:
        try:
            if  fresher.status_id!=None and fresher.status.emailText!="":
                text = fresher.status.emailText
                if fresher.active == False:
                    from IT_show.settings import localHost
                    text = text + "\n激活链接：" + str(localHost) + "/api/signOK/" + fresher.userCode

                user.views.sendEmail(fresher.name, fresher.userCode, fresher.email, text)
                ok1=ok1+1
            else:
                ok2=ok2+1
                messages.warning(request, u"用户" + fresher.name + "当前状态无邮件内容")

        except:
            fail=fail+1
            msg = str(fail) + ".用户" + fresher.name + "的邮件通知发送失败."
            messages.add_message(request, messages.ERROR, msg)
    if ok1>0:
        modeladmin.message_user(request, str(ok1)+"名用户邮件通知发送完成.")
    if ok2 > 0:
        messages.warning(request, str(ok2) + "名用户当前状态无邮件内容.")
    if fail > 0:
        msg = str(fail) + "名用户邮件通知发送失败."
        messages.add_message(request, messages.ERROR, msg)

takeToInfoList.short_description = "将所选用户添加至短信发送列表"


def statusGoBack(modeladmin, request, queryset):
    ok=0
    fail=0
    for fresher in queryset:
            DeleteStatusDetails(fresher.id)
            try:
                nowDetailTail = StatusDetails.objects.get(hostID=fresher, isTail=True)
                fresher.status_id = nowDetailTail.statu.code
                fresher.save()
                ok=ok+1
            except:
                fail=fail+1
                msg = str(fail) + ".用户"+fresher.name+"的撤销操作失败."
                messages.add_message(request, messages.ERROR, msg)

    if ok > 0:
        msg = "已成功撤销了"+str(ok) + "名用户的上一状态改变."
        modeladmin.message_user(request,msg )
    if fail > 0:
        msg = str(fail) + "名用户的撤销操作失败."
        messages.add_message(request, messages.ERROR, msg)

statusGoBack.short_description = "所选用户撤销上一个改变状态的操作"



def activeFresher(modeladmin, request, queryset):
    ok=0
    fail=0
    for fresher in queryset:
            try:
                if fresher.active==False:
                    fresher.active=True
                    newStatu=StatusInfo.objects.get(code=fresher.status_id).nextStatus_id
                    fresher.status_id=newStatu
                    fresher.save()
                    user.views.sendEmail(fresher.name, fresher.userCode, fresher.email,
                                         "激活成功，你的报名信息正在等待审核")

                    newInfo = user.models.StatusDetails.objects.create(statu_id=fresher.status.code, time=datetime.now(),
                                                                       hostID_id=fresher.id,
                                                                       code=user.models.StatusDetails.objects.filter(
                                                                           hostID=fresher.id).count() + 1)
                    ok=ok+1
            except:
                fail=fail+1
    if ok > 0:
        msg = "已成功激活了"+str(ok) + "名用户."
        modeladmin.message_user(request,msg )
    if fail > 0:
        msg = str(fail) + "名用户激活失败."
        messages.add_message(request, messages.ERROR, msg)

activeFresher.short_description = "激活所选用户并发送邮件"

def makeExcel(modeladmin, request, queryset):
    # 创建工作簿
    ws = Workbook(encoding='utf-8')
    w = ws.add_sheet(u"新生报名信息")

    w.write(0, 0, "姓名")
    w.write(0, 1, u"性别")
    w.write(0, 2, u"年级专业")
    w.write(0, 3, u"邮箱")
    w.write(0, 4, u"手机")
    w.write(0, 5, u"自我介绍")
    w.write(0, 6, u"注册时间")
    w.write(0, 7, u"工单号")
    w.write(0,8,u"意向部门")
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
        w.write(excel_row, 2, obj.yearAndMajor)
        w.write(excel_row, 3, obj.email)
        w.write(excel_row, 4, obj.phone)
        w.write(excel_row, 5, obj.selfIntro)
        w.write(excel_row, 6, str(obj.registerTime.strftime("%Y-%m-%d %H:%I:%S")))
        w.write(excel_row, 7, obj.userCode)
        w.write(excel_row, 8, str(obj.wantDepartment))
        excel_row += 1
    # 检测文件是够存在
    # 方框中代码是保存本地文件使用，如不需要请删除该代码
    ###########################
    import os
    fileName = "freshersInfo.xls"
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


# 过滤器

# 新生报名日期
class UserFilterPubtime(admin.SimpleListFilter):
    title = u'注册时间'
    parameter_name = 'registerTime'

    def lookups(self, request, model_admin):
        return (
            ('0', u'今天'),
            ('1', u'本周'),
            ('2', u'本月'),
            ('3', u'今年'),
            ('4', u'今年之前')
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            start = datetime.now() - timedelta(days=1)
            return queryset.filter(registerTime__gte=start)
        elif self.value() == '1':
            start = datetime.now() - timedelta(days=7)
            return queryset.filter(registerTime__gte=start)
        elif self.value() == '2':
            day = datetime.now().day
            start = datetime.now() - timedelta(days=day)
            return queryset.filter(registerTime__gte=start)
        elif self.value() == '3':
            return queryset.filter(registerTime__year=datetime.now().year)
        elif self.value() == '4':
            return queryset.exclude(registerTime__year=datetime.now().year)


# 新生当前状态
class UserFilterStatus(admin.SimpleListFilter):
    title = u'招新状态'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        # info=user.models.StatusInfo.objects.all()[0]
        # temp = (info.code, info.info)
        result = []
        for info in user.models.StatusInfo.objects.all():
            t = (info.code, info.info)
            result.append(t)
        return result

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(status=self.value())


# 新生性别
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

# 新生激活状态
class UserFilterActive(admin.SimpleListFilter):
    title = u'激活状态'
    parameter_name = 'active'

    def lookups(self, request, model_admin):
        return (
            ('0', u'未激活'),
            ('1', u'已激活')
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(active=False)
        elif self.value() == '1':
            return queryset.filter(active=True)

# 新生部门
class UserFilterDepartment(admin.SimpleListFilter):
    title = u'部门'
    parameter_name = 'wantDepartment'

    def lookups(self, request, model_admin):
        result = []
        for info in show.models.Department.objects.all():
            t = (info.id, info.name)
            result.append(t)
        return result

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(wantDepartment=self.value())


# 过滤状态
class StatuFilterPoint(admin.SimpleListFilter):
    title = u'状态内容'
    parameter_name = 'statu__info'

    def lookups(self, request, model_admin):
        result = []
        for info in user.models.StatusInfo.objects.all():
            t = (info.code, info.info)
            result.append(t)
        return result

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(statu__code=self.value())

# 是否链尾
class StatuFilterTail(admin.SimpleListFilter):
    title = u'是否链尾'
    parameter_name = 'isTail'

    def lookups(self, request, model_admin):
        return (
            (False, u'非链尾'),
            (True, u'链尾')
        )

    def queryset(self, request, queryset):
        if self.value() != None:
            return queryset.filter(isTail=self.value())


# 招新管理设置
class FresherAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sex', 'yearAndMajor', "wantDepartment", 'email', 'qqnum', 'phone', 'status', 'registerTime','active')
    search_fields = ('name', 'email', 'phone', 'yearAndMajor',  'qqnum')
    readonly_fields = ["userCode","status","active"]
    list_per_page = 30
    ordering = ('-registerTime',)
    list_filter = (UserFilterActive,UserFilterSex, UserFilterStatus, UserFilterDepartment, UserFilterPubtime,)
    actions = [sendStatuInfo, update_data_src, statusToNext, makeExcel,statusGoBack,activeFresher]
    form = checkForm.FresherForm
    date_hierarchy = 'registerTime'

    class data_src_form(forms.forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        data_src = forms.ModelChoiceField(user.models.StatusInfo.objects)

    class Media:
        css = {
            'all': ('some/path/to/css/disable_save_and_continuue_editing_button.css')
                }


    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        # setNewStatues(obj.id)
        obj.save()



#招生状态设置
class StatusInfoAdmin(admin.ModelAdmin):
    list_display = ('code', 'info', "nextStatus", "emailText")
    search_fields = ('code', 'info', "emailText", "nextStatus__info")
    fieldsets = (
        ["", {
            'fields': ('code', 'info', "emailText", "nextStatus"),
        }],
    )
    readonly_fields = ["code"]
    list_per_page = 30
    ordering = ('-code',)

    def save_model(self, request, obj, form, change):
        # 自定义操作
        obj.save()


# 新生状态详情
class StatusDetailsAdmin(admin.ModelAdmin):
    list_display = ('hostID',  'statu',"info",'code', 'time',"isTail")
    search_fields = ('hostID__name',"statu__info","info")
    readonly_fields = ('hostID',  'statu',"info",'code', 'time',"isTail")
    list_filter = (StatuFilterPoint,StatuFilterTail)
    list_per_page = 30
    ordering = ('-time',)
    actions = []
    # admin.site.disable_action('delete_selected')  # 禁用删除
    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False



    def save_model(self, request, obj, form, change):
        """ 取消后台编辑附件功能 """
        return False


admin.site.site_header = '爱特展示网后台管理'
admin.site.site_title = '后台管理'
admin.site.index_title = '爱特展示网'

admin.site.register(Fresher, FresherAdmin)
admin.site.register(StatusInfo, StatusInfoAdmin)
admin.site.register(StatusDetails, StatusDetailsAdmin)
