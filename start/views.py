from django.shortcuts import render



# from Gogo import settings

def start_view(request):
    # print(settings.lol)
    return render(request, 'start_view.html')

#
# def create(request):
#     return render(request,'start_view.html')


def question_1(request):
    return render( request, "question_1.html")

# def identify(request):



# Create your views here.
