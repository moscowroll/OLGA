from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.registration),
    path('create/', views.create),
    path('question_1', views.question_1)

]
