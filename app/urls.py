from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('demo', views.demo, name='demo'),
    path('legal', views.legal, name='legal'),
    path('login', views.login, name='login'),
    path('careers', views.careers, name='careers'),
    path('about', views.about, name='about'),

]