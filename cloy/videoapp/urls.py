from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=''),
    path('uploader/', views.uploader, name='uploader'),
]
