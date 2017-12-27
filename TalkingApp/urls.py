# -*- coding: utf-
# from django.urls import HttpResponse

# def index(request):
# 	return HttpResponse("Hello! How are you")

# # Create your views here.

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getUserName/$', views.getUserName, name='getUserName'),
]