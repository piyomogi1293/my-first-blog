from django.urls import path
from . import views

utlpatterns = [
    path('', views.post_list, name='post_list'),
]