from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


# def index(request):
#    return render(request, 'home.html')


def index(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home.html', {'string': string})


def test1(request):
    return render(request, 'test1.html')


def test2(request):
    return render(request, 'test2.html')



