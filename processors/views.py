from django.shortcuts import render
from rest_framework import viewsets
from .models import Processors
from .serializers import ProcessorSerializer

class ProcessorView(viewsets.ModelViewSet):
    queryset = Processors.objects.all()
    serializer_class = ProcessorSerializer 