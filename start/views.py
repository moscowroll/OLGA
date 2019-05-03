from django.shortcuts import render

from django.http import HttpResponse

# from Gogo import settings

def start_view(request):
    # print(settings.lol)
    return render(request, 'start_view.html')

#
# def create(request):
#     return render(request,'start_view.html')


def question_1(request):
    print('________________')
    print(request)
    print('________________')
    return render( request, "question_1.html")

# def identify(request):





def check_first(request):
    if request.user.is_authenticated:
        return HttpResponse('vse kayf')
    else:
        return HttpResponse('vse ne ice suka blyat')
# Create your views here.
