"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers,serializers,viewsets,status
from polls.models import TblCustomer
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mysite.views import *

urlpatterns = [
   # url(r'^api-auth/$', get_customer_list),
   # url(r'^api-auth/get_customer/weixinOpenId=(?P<weixinOpenId>.{28})nickname=(?P<nickname>.*)sex=(?P<sex>[0-9]{1})$', get_customer),
   # url(r'^api-auth/get_bodys/weixinOpenId=(?P<weixinOpenId>.{28})$', get_bodys),
   # url(r'^api-auth/create_body/weixinOpenId=(?P<weixinOpenId>.{28})name=(?P<name>.*)h=(?P<h>.*)w=(?P<w>.*)bshape=(?P<bshape>.*)fshape=(?P<fshape>.*)fcolor=(?P<fcolor>.*)$', create_body),
   # url(r'^api-auth/get_matches/weixinOpenId=(?P<weixinOpenId>.{28})$', get_matches),
   # url(r'^api-auth/get_match_pic/matchId=(?P<matchId>.*)$', get_match_pic),
   url(r'^api-auth/get_customer/$', get_customer),
   url(r'^api-auth/get_bodys/$', get_bodys),
   url(r'^api-auth/create_body/$', create_body),
   url(r'^api-auth/get_matches/$', get_matches),
   url(r'^api-auth/get_match/$', get_match),
   url(r'^api-auth/get_recommend/$',get_recommend),
]
urlpatterns = format_suffix_patterns(urlpatterns)
