from django.db import models


class Member(models.Model):
    name = models.CharField(verbose_name="名字", max_length=10, default="")
    photo = models.ImageField(verbose_name="皂片", upload_to='show/member_photo')
    intro = models.TextField(verbose_name="个性签名", max_length=100, default="")
    year = models.IntegerField(verbose_name="年份", default=0)

    class Meta:
        verbose_name = r"成员信息"
        verbose_name_plural = r"成员信息"
        get_latest_by = "year"

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(verbose_name="部门名", max_length=10, default="")
    pic = models.ImageField(verbose_name="图标", upload_to='show/department_pic')
    intro = models.TextField(verbose_name="部门介绍", max_length=100, default="")

    class Meta:
        verbose_name = r"部门"
        verbose_name_plural = r"部门"

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(verbose_name="事件名", max_length=10, default="")
    pic = models.ImageField(verbose_name="配图", upload_to='show/department_pic')
    content = models.TextField(verbose_name="详细内容", max_length=100, default="")
    year = models.IntegerField(verbose_name="年份", default=0)

    class Meta:
        verbose_name = r"爱特大事记"
        verbose_name_plural = r"爱特大事记"
        get_latest_by = "year"

    def __str__(self):
        return self.name


class WorksShow(models.Model):
    name = models.CharField(verbose_name="网站名", max_length=10, default="")
    pic = models.ImageField(verbose_name="网站图片", upload_to='show/WorksShow_pic')
    link = models.TextField(verbose_name="链接", default="")

    class Meta:
        verbose_name = r"成果展示"
        verbose_name_plural = r"成果展示"

    def __str__(self):
        return self.name


class HeadPicture(models.Model):
    name = models.CharField(verbose_name="描述", max_length=10, default="")
    pic = models.ImageField(verbose_name="图片", upload_to='show/WorksShow_pic')

    class Meta:
        verbose_name = r"匿名评论头像"
        verbose_name_plural = r"匿名评论头像"

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.CharField(verbose_name="内容", max_length=100, default="")
    head = models.ForeignKey(HeadPicture, verbose_name="头像", null=True, on_delete=models.SET_NULL)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = r"匿名评论"
        verbose_name_plural = r"匿名评论"

    def __str__(self):
        return self.content
