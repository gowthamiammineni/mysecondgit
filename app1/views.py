from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def object(request):
    return HttpResponse('object is created by using class name')
def Navya(request):
    return HttpResponse('Navya eats daily')
def Class(request):
    return HttpResponse('Class is created by using class keyword')