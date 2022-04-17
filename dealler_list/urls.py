from django.urls import path
from . import views

urlpatterns = [
    path('', views.deallerdata),
    path('mytable/', views.getmytable),
    path('mytable/<str:pk>/', views.getmytable),
]