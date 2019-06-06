from django import forms
from blogapp.models import Blog
from django.contrib.auth.models import User

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('name','body','pic')

class Signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')
