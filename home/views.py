from django.shortcuts import render
import csv
import io
from io import BytesIO
from django.http import HttpResponse
from django.views.generic import View
import hashlib
import urllib,json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import *
# Create your views here.
class Uploadcsvs(APIView):
    parser_classes = [MultiPartParser,FormParser]
    
    def post(self, request ,format=None):

        fetchData=Uploadcsv.objects.all()
        csv_file=request.data['csv']
        if not csv_file.name.endswith('.csv'):
            
            messages.error(request,'This is not a csv File, upload a csv file!!')
        data_set=csv_file.read().decode('UTF-8')
        io_string=io.StringIO(data_set)
                  
        for col in csv.DictReader(io_string):
         
            Uploadcsv.objects.update_or_create(firstname=col['firstname'],email=col['email'],address=col['address'])
        # serializing the fecthed data--
        serializer= UploadcsvSerializers(fetchData, many=True)
            
        return JsonResponse({'message':'success','data':serializer.data})
            
        return Response(status=204)

