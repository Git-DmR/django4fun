from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    news = News.objects.all()
    result = '<h1>List of news.</h1>\n'
    for item in news:
        result += f"<div>\n<h2>{item.title}:<h2>\n<p>{item.content}</p>\n</div></hr>"

    return HttpResponse(result)

def test(request):
    return HttpResponse("<H1>Test page!!</H1>")