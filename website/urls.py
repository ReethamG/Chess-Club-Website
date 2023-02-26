from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources, name='resources'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('join/', views.join, name='join'),
    path('about/', views.about_us, name='about_us'),
]