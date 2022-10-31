from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #print(dir(request))
    return HttpResponse("<H2>Hello World !!!</H2>")

def test(request):
    return HttpResponse("<H1>Test page!!</H1>")