from django.shortcuts import render,HttpResponseRedirect

from .forms import UserForm

from .  import models

def registration(request):

    reg_form = UserForm()

    return render(request, 'registration.html', {"form" : reg_form})




def create(request):
    if request.method == "POST":
        someone = models.Person()
        someone.name = request.POST.get("name")
        someone.birth_date = request.POST.get("birth_date")
        someone.gender = request.POST.get("gender")
        someone.save()
    return HttpResponseRedirect("/")




# Create your views here.
