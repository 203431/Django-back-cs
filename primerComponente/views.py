from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from multiprocessing import context

# Importaciones de modelo
from primerComponente.models import PrimerTabla

# importaciones de serializadores 
from primerComponente.serializers import PrimerTablaSerializers

# Create your views here.
class PrimerTablaList(APIView):
    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializers = PrimerTablaSerializers(queryset, many=True, context={'request': request})
        return Response(serializers.data)