from django.contrib import admin
from django.urls import path, include

from . import views



urlpatterns =  [

    path('', views.start_view),
    path('identify/', include('registration.urls')),
    # path('crate', views.create),
    path('question_1/', views.question_1),
    path('check_first/', views.check_first)




]
