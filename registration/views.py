from django.shortcuts import render,HttpResponseRedirect

from django.contrib import auth


from .forms import UserForm
from . import forms

from .  import models

def registration(request):

    reg_form = UserForm()

    return render(request, 'registration.html', {"form" : reg_form})



def create(request):
    # print('soski')
    if request.method == "POST":
        someone = models.Person()
        someone.name = request.POST.get("name")
        someone.age = request.POST.get("age")
        someone.gender = request.POST.get("gender")
        someone.login = request.POST.get("login")
        print(someone.name)
        print(someone.age)
        print(someone.gender)
        print(someone.login)
        someone.save()
        # new_user_form = Reg(request.POST)

        # new_user = new_user_form.save()
            # new_user = auth.authenticate(username = new_user_form.cleaned_data['login'], password = new_user_form.cleaned_data['age'])
        auth.login(request, someone, backend='django.contrib.auth.backends.ModelBackend')



    return HttpResponseRedirect("/question_1/")


def question_1(request):
    return render(request, "question_1.html")


# Create your views here.
