from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    #path('contact/', views.contact, name="contact"),
    #path('blog/', views.blog, name="blog"),
    
]

