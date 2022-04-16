from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# generic base view
from django.views.generic import TemplateView 









# Create your views here.
def aboutus(request):
    return render(request, 'about-us.html', {'Dealler': 'Dealler office Location'})


def contactus(request):
    return render(request, 'contactus.html', {'Dealler': 'Dealler call back request'})

def HomePageView(request):
    return render(request, 'about-us.html', {'Dealler': 'Dealler office Location'})


