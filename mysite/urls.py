from django.urls import path, include
from . import views

urlpatterns = [
    path('home.html',views.home, name="home"),   
]