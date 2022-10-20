from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from .models import *

from django.core.files.base import ContentFile
import io
from django.core.files.images import ImageFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.layout import Button


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='conform password', widget=forms.PasswordInput())
    
    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
    helper.add_input(
        Button(
            "cancel",
            "Cancel",
            css_class="btn",
            onclick=f"javascript:location.href = '';",
        )
    )
    helper.form_method = "POST"

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
        fields = ['image','addpost']
        

class Addposts(forms.ModelForm):  
    images = forms.ImageField(
        label='image',
        widget=forms.ClearableFileInput(attrs={"multiple": True}))
  
    class Meta:
        model = Addpost
        fields = ['title', 'desc', 'date', 'images']
        exclude = ['likes']
     
    def save(self, commit=True):
        images = self.cleaned_data.pop('images')
        data = super(Addposts, self).save(commit=False)
        if commit:
            data.save()
            print(images)
            # if len(images) == 1:
            Image.objects.create(image=images, addpost=data)
            # else:
                # for image in images:
                #     img = ImageFile(io.BytesIO(image), name=f"{data.title}.jpg")
        return data
  
    # def save(self, commit=True):
    #     print()
    #     print(self.cleaned_data ,'*******',self.cleaned_data['image'].name)
    #     addpost = Addpost.objects.create(title=self.cleaned_data['title'],
    #                                      desc = self.cleaned_data['desc'],
    #                                      date = self.cleaned_data['date'],
    #                                      )
    #     addpost.save()
    #     image = Image.objects.create(image = self.cleaned_data['image'],addpost = addpost)
    #     image.save()
    #     print(image, addpost, "------4-------") 
    #     print("successfully")
    #     return addpost
        


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'fname', 'lname', 'country']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'comment']
