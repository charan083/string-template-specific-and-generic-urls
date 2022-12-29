from django.urls import path
from app1.views import *
app_name='somthing1'

urlpatterns=[
    path('firststring/',firststring,name='firststring')
]