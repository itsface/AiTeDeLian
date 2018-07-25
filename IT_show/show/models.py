from django.db import models
from django.utils.safestring import mark_safe
import IT_show.settings


class Department(models.Model):
    name = models.CharField(verbose_name="部门名", max_length=10, default="")
    pic = models.ImageField(verbose_name="图标", upload_to='image/DepartmentPicture/',default='media/default/DepartmentPicture.png', max_length=100)
    intro = models.TextField(verbose_name="部门介绍", max_length=500, default="")
    existing = models.BooleanField(verbose_name="是否存留", default=True)

    class Meta:
        verbose_name = r"部门"
        verbose_name_plural = r"部门"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img width=50px src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.pic))

class Member(models.Model):
    Gender_Choice = (
        (False, u'男'),
        (True, u'女')
    )
    sex = models.BooleanField(verbose_name="性别", default=False, choices=Gender_Choice,blank=True)
    name = models.CharField(verbose_name="名字", max_length=10, default="")
    photo = models.ImageField(verbose_name="皂片", upload_to='image/MemberPhoto/',default='media/default/MemberPhoto.png',)
    intro = models.TextField(verbose_name="个性签名", max_length=100, default="")
    year = models.IntegerField(verbose_name="年份", default=0)
    department=models.ForeignKey(Department,verbose_name="所属部门", max_length=10, default="",null=True)

    class Meta:
        verbose_name = r"成员信息"
        verbose_name_plural = r"成员信息"
        get_latest_by = "year"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img width=50px src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.photo))

    def fullImage(self):
        return mark_safe('<img src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.photo))



class Event(models.Model):
    name = models.CharField(verbose_name="事件名", max_length=10, default="")
    pic = models.ImageField(verbose_name="配图", upload_to='image/EventPhoto/',default='media/default/EventPhoto.png',)
    content = models.TextField(verbose_name="详细内容", max_length=100, default="")
    year = models.IntegerField(verbose_name="年份", default=0)

    class Meta:
        verbose_name = r"爱特大事记"
        verbose_name_plural = r"爱特大事记"
        get_latest_by = "year"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img width=50px src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.pic))



class WorksShow(models.Model):
    name = models.CharField(verbose_name="网站名", max_length=10, default="")
    pic = models.ImageField(verbose_name="网站图片",upload_to='image/WorksShowPhoto/',default='media/default/WorksShowPhoto.png',)
    link = models.TextField(verbose_name="链接", default="")

    class Meta:
        verbose_name = r"成果展示"
        verbose_name_plural = r"成果展示"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img width=100px src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.pic))

class HeadPicture(models.Model):
    name = models.IntegerField(verbose_name="序号", default=-1)
    pic = models.ImageField(verbose_name="图片", upload_to='image/HeadPicture/',default='image/default/HeadPicture.png', max_length=100)

    class Meta:
        verbose_name = r"匿名评论头像"
        verbose_name_plural = r"匿名评论头像"

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        return mark_safe('<img width=50px src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.pic))

    def save(self, *args, **kwargs):
        from base import func
        if self.name=="" or self.name==-1:
            try:
                self.name=HeadPicture.objects.all().order_by("-name")[0].name + 1
            except:
                self.name=100
        super(HeadPicture, self).save(*args, **kwargs)  # Call the "real" save() method.

    # def delete(self, using=None, soft=True, *args, **kwargs):
    #     name=self.name
    #     if name!=0 or name !="0":
    #         print(name)
    #         code=self.id
    #         results = Comment.objects.filter(head__comment__code=code)
    #         defaultId=0
    #         try:
    #             defaultId=HeadPicture.objects.get(name=0).id
    #         except:
    #             defaultId=HeadPicture.objects.all().order_by("name")[0].id
    #
    #         for one in results:
    #             try:
    #                 one.head_id=defaultId
    #                 one.save()
    #             except:
    #                 pass
    #         super(HeadPicture, self).delete(using=using, *args, **kwargs)




class Comment(models.Model):
    code = models.IntegerField(verbose_name="这是第几个创建的评论",primary_key=True,auto_created=True,default=-1)
    name=models.CharField(verbose_name="昵称",max_length=10,default="")
    content = models.TextField(verbose_name="内容", max_length=100, default="")
    reply=models.TextField(verbose_name="回复",max_length=200,default=None,null=True,blank=True)
    head = models.ForeignKey(HeadPicture, verbose_name="头像", null=True, on_delete=models.SET_NULL,default=0)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = r"评论"
        verbose_name_plural = r"评论"


    def __str__(self):
        return self.content

    def image_tag(self):
        if self.head.pic !=None:
            return mark_safe('<img width=50px src="%s%s" />' % (IT_show.settings.MEDIA_URL,self.head.pic))

    def save(self, *args, **kwargs):
        if self.code==-1:
            try:
                self.code=Comment.objects.all().order_by("-code")[0].code+1
            except:
                self.code=100
        super(Comment, self).save(*args, **kwargs)

