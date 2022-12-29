from django.urls import path
from app2.views import *
app_name='somthing2'

urlpatterns=[
    path('string1/',string1,name='string1')
]