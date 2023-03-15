from django.urls import path
from . import views

urlpatterns = [
    path('qwer/', views.hahaha, name='qwer'), #함수 greeting을 불러올 것이다.
    path('asdf/', views.hohoho, name='asdf'),
]