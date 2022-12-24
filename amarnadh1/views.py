from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def joshna(request):
    return HttpResponse('<b>she is a beautiful</b>')

def lucky(request):
    return HttpResponse('<i>qqwertyasdfghj</i>')  

def navyasri(request):
    return HttpResponse('<h1><marquee>litle princess</marquee></h1>')  
