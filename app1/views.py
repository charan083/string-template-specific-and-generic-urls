from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firststring(request):
    return render(request,'app1(1).html')