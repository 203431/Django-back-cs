from cmath import exp
from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from multiprocessing import context
from rest_framework import status
# Importación json
import json


# Importaciones de modelo
from primerComponente.models import PrimerTabla

# importaciones de serializadores 
from primerComponente.serializers import PrimerTablaSerializers

# Create your views here.

responseOk = '{"messages":"success", "payload": "serializer.data","status":"status"}'
responseOk = json.loads(responseOk)




class PrimerTablaList(APIView):
    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializers = PrimerTablaSerializers(queryset, many=True, context={'request': request})
        return Response(responseOk)
        
    def post(self, request, format=None):
        serializer = PrimerTablaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def jsonMaker(self, message, data, status):
        json1 = {"message":message, "pay_load":data, "status":status }
        dumper=json.dumps(json1)
        responseOk = json.loads(dumper)
        return responseOk


    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializers(queryset, many = True, context = {'request':request})
        responseOk = self.jsonMaker("succes", serializer.data, status.HTTP_200_OK)
        return Response(responseOk)

class PrimerTablaDetail(APIView):
    def get_objet(self, pk):
        try: 
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        print(pk)
        idResponse = self.get_objet(pk)
        if idResponse != 0:
            idResponse = PrimerTablaSerializers(idResponse)
            return Response(idResponse.data, status= status.HTTP_200_OK)
        return Response("No hay datos", status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_objet(pk)
        serializer = PrimerTablaSerializers(idResponse, data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deleteObj = self.get_object(pk)
        if deleteObj != 0:
            id = pk
            deleteObj.delete()
            return Response("DATO ELIMINADO: " + id, status= status.HTTP_200_OK)
        return Response("No hay datos", status=status.HTTP_400_BAD_REQUEST)
            
