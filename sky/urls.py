from django.urls import path
from sky import views as sky_views

from django.conf.urls import include


app_name = 'sky'
urlpatterns = [
    path('test3/', sky_views.test3, name='test3'),
    path('test4/', sky_views.test4, name='test4'),
    path('test5/', sky_views.test5, name='test5'),
    path('base/', sky_views.base, name='base'),
    path('hostInput/', sky_views.hostInput, name='hostInput'),
]
