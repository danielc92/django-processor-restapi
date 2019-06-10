from django.shortcuts import render
from rest_framework import viewsets
from .models import Processors, Manufacturer, ProductSeries
from .serializers import ProcessorSerializer, ManufacturerSerializer, ProductSeriesSerializer


class ProcessorView(viewsets.ModelViewSet):
    queryset = Processors.objects.all()
    serializer_class = ProcessorSerializer 


class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer 


class ProductSeriesView(viewsets.ModelViewSet):
    queryset = ProductSeries.objects.all()
    serializer_class = ProductSeriesSerializer 