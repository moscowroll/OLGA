from django.shortcuts import render

from .forms import UserForm

def registration(request):

    reg_form = UserForm()

    return render(request, 'registration.html', {"form" : reg_form})
# Create your views here.
