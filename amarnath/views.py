from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sriram(request):
    return HttpResponse('<marquee><h1>my fav god</h1></marquee>')


def sitha(request):
    return HttpResponse('<h1>one and only princess</h1>')    


def lavakusa(request):
    return HttpResponse('<marquee><h1>* * * * * *</h1></marquee>')    