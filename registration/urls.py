from django.contrib import admin
from django.urls import path, include

from . import views

from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = [
    # path('', views.registration), # регаемся
    path('', auth_views.LoginView.as_view(),{'authentication_form': LoginForm} ),
    path('create/', views.create),
    path('create_user/', views.create_user),
    path('question_1', views.question_1)

]
