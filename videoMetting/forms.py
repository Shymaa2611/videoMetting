from django.contrib.auth.models import User
from django import forms



class signUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','password','email']


      