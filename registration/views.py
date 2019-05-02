from django.shortcuts import render,HttpResponseRedirect

from .forms import UserForm

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
    return HttpResponseRedirect("/question_1/")


def question_1(request):
    return render(request, "question_1.html")


# Create your views here.
