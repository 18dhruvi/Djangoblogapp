from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from .models import *



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='conform password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class LoginForm(AuthenticationForm):
    username = UsernameField()
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = []


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='image',
        widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Image
        fields = ['image']
        

class Addposts(ImageForm):  
    
    # def __init__(self,*args, **kwargs):
    #     super(Addposts, self).__init__(*args, **kwargs)
  
    class Meta:
        model = Addpost
        fields = ['title', 'desc', 'date']
        exclude = ['likes']
     # image = forms.ImageField(label='image',widget=forms.ClearableFileInput(attrs={"multiple": True}),)
     

         
     



class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'fname', 'lname', 'country']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'comment']
