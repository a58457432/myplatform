"""myplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import captcha
from django.contrib import admin
from django.urls import path
from calc import views as calc_views
from login import views as login_views
from django.conf.urls import include
from captcha import *
from calc import views
from login import views
from sky import views


urlpatterns = [
    #    path('', dbmp_views.index),
    #    path('', calc_views.index, name='home'),
    #    path('add/', calc_views.add, name='add'),
    #    path('new_add/<int:a>/<int:b>/', calc_views.add2, name='add2'),
    #    path('index/', login_views.index, name='index'),
    #    path('login/', login_views.login, name='login'),
    #    path('register/', login_views.register, name='register'),
    #    path('logout/', login_views.logout, name='logout'),
    #    path('test/', login_views.test, name='test'),
    path('admin/', admin.site.urls),
    #    path('captcha/',  captcha.urls),
    path('captcha/', include('captcha.urls')),
    #    path('test1', calc_views.test1, name='test1'),
    #    path('test2', calc_views.test2, name='test2'),
    path('', include('login.urls', namespace='login')),
    path('calc/', include('calc.urls', namespace='calc')),
    path('sky/', include('sky.urls', namespace='sky')),
]
