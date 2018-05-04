from django.db import models


class Fresher(models.Model):
    name = models.TextField(verbose_name="姓名", max_length=10, default="")
    sex = models.BooleanField(verbose_name="性别", default=False)
    # 0False男 1True女
    yearAndMajor = models.TextField(verbose_name="年级专业", max_length=20, default="")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.TextField(verbose_name="手机号", max_length=15, default="")
    selfIntro = models.TextField(verbose_name="自我介绍", max_length=300, default="")
    status = models.IntegerField(verbose_name="招新状态", default=0)
    registerTime = models.DateTimeField(verbose_name="注册时间", auto_now_add=True)

    class Meta:
        verbose_name = r"报名者"
        verbose_name_plural = r"报名者"
        get_latest_by = "registerTime"

    def __str__(self):
        return self.name
