from django.urls import  path
from . import views

urlpatterns = [ 
    path('aboutus/', views.aboutus),
    path('contactus/',views.contactus),
    path('', views.aboutus),
]