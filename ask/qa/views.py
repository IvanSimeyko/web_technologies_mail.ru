from django.shortcuts import render

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    return render(request, 'index.html', )