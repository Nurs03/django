from django import forms
from .models import Clothes, Customs,User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class Clothesform(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    info= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter info'})
    image = forms.FileField(required=False,widget= forms.FileInput(attrs={ 'class':'form-control'}))
   
    class Meta:
        model=Clothes
        fields="__all__"        

class Customsform(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    info= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter info'})
    image = forms.FileField(required=False,widget= forms.FileInput(attrs={ 'class':'form-control'}))
   
    class Meta:
        model=Customs
        fields="__all__"


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    birthdate = forms.DateField()
    discord_id = forms.CharField(max_length=100, label='Discord ID')
    zoom_id = forms.CharField(max_length=100, label='Zoom ID')


    class Meta:
        model = User
        fields = ["username", "birthdate", "email", "discord_id", "zoom_id"]


class EmailForm(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)



#
# # class NewUserForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ["username","birthdate", "email", "discord_id", "zoom_id"]

