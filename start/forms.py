from django import forms

class identifyForm(forms.form):
    name = forms.CharField()
    age = forms.IntegerField()
    
