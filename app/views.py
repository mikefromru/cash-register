from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import ItemSerializer
from rest_framework.renderers import JSONRenderer

@api_view(['POST'])
def load_bill(request):
    # if request.method == 'POST':
    json = request.data
    # print(json)
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        print(serializer.data)
        return Response(serializer.data)
