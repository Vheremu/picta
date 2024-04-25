
from django import forms
from django.contrib.auth.models import User
from fp.models import Pop

class POPFORM(forms.ModelForm):
    class Meta():
        model = Pop
        fields = ('account','pop','popid',)