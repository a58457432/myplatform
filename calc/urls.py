from django.urls import path
from calc import views as calc_views

from django.conf.urls import include


app_name = 'calc'
urlpatterns = [
    path('', calc_views.index, name='home'),
    path('add/', calc_views.add, name='add'),
    path('new_add/<int:a>/<int:b>/', calc_views.add2, name='add2'),
    path('test1', calc_views.test1, name='test1'),
    path('test2', calc_views.test2, name='test2'),
]
