from django import forms
from . import models

# class UserForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
#     age = forms.DateField(widget=forms.TextInput(attrs={"class":"myfield"}))
#     gender = forms.ChoiceField(choices=((1, "Male"), (2, "Female")), widget=forms.Select(attrs={'class':'myfield'}))
#
#     # , widget=forms.TextInput(attrs={"class":"choices_2"})
#     class Meta:
#         model = models.Person
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'circle'}),
#             'age ': forms.TextInput(attrs={'class':'circle'}),
#             'gender': forms.TextInput(attrs={'class':'circle ma_fema'}),
#
#         }



class UserForm(forms.ModelForm):

    class Meta:
        model = models.Person
        fields = (
                 'name',
                 'login',
                 'age',
                 'gender'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myfield'}),
            'login': forms.TextInput(attrs={'class': 'myfield'}),
            'age': forms.TextInput(attrs={'class': 'myfield'}),
            'gender': forms.TextInput(attrs={'class': 'myfield'})
        }




from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
