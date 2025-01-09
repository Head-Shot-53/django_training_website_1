from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    return HttpResponse('Hello world')

def second_page(request):
    a = '<h1>Hello world<h1>'
    text = 'Hello'
    return render(request, './index.html',{
        'a':a,
        'text': text
    })