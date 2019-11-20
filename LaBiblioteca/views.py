from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.

def HomepageView(request):
    return HttpResponse("Witaj na stronie głównej.")