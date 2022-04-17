from rest_framework.decorators import api_view
from rest_framework.response import Response
from dealler_list.models import models
from .serializers import mytableSerializer
from dealler_list import serializers
from django.shortcuts import render

def deallerdata(request):
    deallers = dealler_list_dealist.object.all()
    dealDict = {'deallers': deallers}
    return render(request, 'dealler_list/about-us.html',dealDict) 



@api_view(['GET'])
def getmytable(request):
    routes = [
        'GET /api',
        'GET /api/mytable',
        'GET /api/mytable/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getmytable(request):
    mytable = models.objects.all()
    serializer = mytableSerializer(mytable, many=True)
    return Response(serializer.data)

