from django.shortcuts import render

# Create your views here.


def test3(request):
    return render(request, 'sky/test3.html')


def test4(request):
    return render(request, 'sky/test4.html')


def test5(request):
    return render(request, 'sky/test5.html')


def base(request):
    return render(request, 'sky/base.html')


def hostInput(request):
    return render(request, 'sky/hostInput.html')




