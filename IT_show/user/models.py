from django.db import models
import show.models


class StatusInfo(models.Model):
    code=models.IntegerField(verbose_name="状态Id", default=0, auto_created=True, primary_key=True)
    nextStatus = models.ForeignKey('self', verbose_name="下个状态", null=True, blank=True, on_delete=models.SET_NULL)
    # nextStatus = models.IntegerField(verbose_name="下个状态", null=True)
    info=models.CharField(verbose_name="状态信息",max_length=50)
    emailText = models.TextField(verbose_name="邮件主体", max_length=50,default="",null=True,blank=True,help_text="留空则表示该状态不发送信息")

    class Meta:
        verbose_name = r"状态内容维护"
        verbose_name_plural = r"状态内容维护"

    def __str__(self):
        return str(self.info)


class Fresher(models.Model):
    Gender_Choice = (
        (False, u'男'),
        (True, u'女')
     )
    name = models.CharField(verbose_name="姓名", max_length=10, default="")
    sex = models.BooleanField(verbose_name="性别", default=False,choices=Gender_Choice)
    # 0False男 1True女
    yearAndMajor = models.CharField(verbose_name="年级专业", max_length=20, default="")
    email = models.EmailField(verbose_name="邮箱")
    qqnum = models.CharField(verbose_name="qq号", max_length=12, default="")
    phone = models.CharField(verbose_name="手机号", max_length=15, default="")
    selfIntro = models.TextField(verbose_name="自我介绍", max_length=300, default="")
    status = models.ForeignKey(StatusInfo,verbose_name="招新状态",default=0,null=True,blank=True,on_delete=models.SET_NULL)
    wantDepartment = models.ForeignKey(show.models.Department,verbose_name="意向部门", max_length=10, default="",null=True)
    #wantDepartment=models.CharField(verbose_name="意向部门",max_length=10,default="",choices=Department_Choice)
    #status = models.IntegerField(verbose_name="招新状态", default=0)
    registerTime = models.DateTimeField(verbose_name="报名时间", auto_now_add=True)
    userCode=models.CharField(verbose_name="工单号",max_length=10, default="")
    active = models.BooleanField(verbose_name="是否激活", default=False)

    class Meta:
        verbose_name = r"报名者"
        verbose_name_plural = r"报名者"
        get_latest_by = "registerTime"

    def __str__(self):
        return self.name


class StatusDetails(models.Model):
    code = models.IntegerField(verbose_name="链中位置")
    time = models.DateTimeField(verbose_name="发生时间", auto_now_add=True)
    info = models.CharField(verbose_name="额外信息", max_length=50, default="", blank=True, null=True, help_text="额外信息选填")
    hostID = models.ForeignKey(Fresher, verbose_name="报名者")
    isTail = models.BooleanField(verbose_name="是否链末尾", default=True)
    statu = models.ForeignKey(StatusInfo, verbose_name="状态", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = r"报名者状态链"
        verbose_name_plural = r"报名者状态链"

    def __str__(self):
        return self.hostID.name
