from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Agora'),
    path('archive/', views.archive, name='Agora-Archive'),
]
