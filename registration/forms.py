from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    birth_date = forms.DateField()
    gender = forms.ChoiceField(choices=((1, "Male"), (2, "Female")))
