from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializer import *
from rest_framework.decorators import api_view

# Create your views here.

@api_view()
def msgs(request):
    return Response({"message": "Hello, world!"})

class infos(APIView):
    def get(self, request):
        outputmsg = info.objects.all()
        serializer = infoSerializer(outputmsg, many=True)
        return Response(serializer.data)
