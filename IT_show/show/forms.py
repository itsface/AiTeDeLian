from django import forms
from datetime import datetime
import re
from show.models import *

#爱特成员信息表单验证
class MenberForm(forms.ModelForm):
    def clean_intro(self):
        data = self.cleaned_data['intro']
        if data =="" or data==None:
            raise forms.ValidationError("个性签名不能为空!")
        return data

    def clean_year(self):
        data = self.cleaned_data['year']
        if int(data) > datetime.now().year:
            raise forms.ValidationError("成员年份不能大于当前年份!")
        elif int(data) <2000:
            raise forms.ValidationError("成员年份似乎不正确!")
        return data

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data)<2 or len(data)>10:
            raise forms.ValidationError("名字长度有误（2-10)!")
        return data

    def clean(self):
        return self.cleaned_data

#大事记表单验证
class EventForm(forms.ModelForm):
    def clean_year(self):
        data = self.cleaned_data['year']
        if int(data) > datetime.now().year:
            raise forms.ValidationError("大事件年份不能大于当前年份!")
        elif int(data) <2000:
            raise forms.ValidationError("大事件年份似乎不正确!")
        return data


#新生信息表单验证
class FresherForm(forms.ModelForm):
    def clean_qqnum(self):
        data = self.cleaned_data['qqnum']
        pattern = r"[1-9]\d{4,109}"
        res = re.search(pattern, data)
        if res:
            return data
        else:
            raise forms.ValidationError("QQ号输入有误!")

    def clean_phone(self):
        data = self.cleaned_data['phone']
        pattern = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        res = re.search(pattern, data)
        if res :
            return data
        else:
            raise forms.ValidationError("手机号输入有误!")

    def clean_email(self):
        data = self.cleaned_data['email']
        pattern = r"[-_\w\.]{0,64}@([-\w]{1,63}\.)*[-\w]{1,63}"
        res = re.search(pattern, data)
        if res:
            from user.models import Fresher
            if Fresher.objects.filter(email=data).count() <= 3:
                return data
            else:
                raise forms.ValidationError("该邮箱注册超过3次，禁止注册!")
        else:
            raise forms.ValidationError("邮箱输入有误!")

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data)<2 or len(data)>10:
            raise forms.ValidationError("名字长度有误（2-10)!")
        return data

    def clean_yearAndMajor(self):
        data = self.cleaned_data['yearAndMajor']
        pattern = r"\d{4}\S{2,10}"
        res = re.search(pattern, data)
        if res:
            return data
        else:
            raise forms.ValidationError("年级专业输入有误!")

#部门信息表单验证
class DepartmentForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        result=Department.objects.filter(name=data)
        if len(result)==0:
            return data
        else:
            raise forms.ValidationError("部门名称不能重复!")