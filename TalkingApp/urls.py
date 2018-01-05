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

from django.conf.urls import include, url
# from rest_framework import routers
from TalkingApp import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)
# router.register(r'userLogging', views.UserLoggingViewSet)
# router.register(r'myObjects', views.UserLoggingViewSet, base_name='UserLoggingViewSet')

# urlpatterns = [
#     # url(r'^$', views.index, name='index'),
#     # url(r'^getUserName/$', views.getUserName, name='getUserName'),
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]



 
urlpatterns = [
    url(r'^userLogging/$', views.UserLogging_list),
    url(r'^getOnlineList/$', views.Get_Online_list),
    url(r'^user_new/$', views.User_pussh),
    url(r'^Get_female/$', views.Get_female),
]
urlpatterns = format_suffix_patterns(urlpatterns)