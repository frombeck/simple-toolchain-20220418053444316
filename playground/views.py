from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aboutus(request):
    return render(request, 'about-us.html', {'Dealler': 'Dealler office Location'})


def contactus(request):
    return render(request, 'contactus.html', {'Dealler': 'Dealler call back request'})
