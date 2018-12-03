from django.urls import path
from login import views as login_views

app_name = 'login'

urlpatterns = [
    path('index/', login_views.index, name='index'),
    path('login/', login_views.login, name='login'),
    path('register/', login_views.register, name='register'),
    path('logout/', login_views.logout, name='logout'),
    path('test/', login_views.test, name='test'),
]
