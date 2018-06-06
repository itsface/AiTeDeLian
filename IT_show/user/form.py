from django import forms
from .models import Fresher


class FresherForm(forms.ModelForm):

    class Meta:
        model = Fresher
        exclude = ['status', 'registerTime', 'userCode', 'active']
