from rest_framework import serializers as s
from .models import Processors, Manufacturer, ProductSeries


class ProcessorSerializer(s.ModelSerializer):
    class Meta:
        model = Processors
        fields = ('id','core_count','thread_count', 'tdp_watts', 'model_name', 
        'model_series','manufacturer', 'rrp_usd', 'base_clock', 'turbo_clock', 
        'created_at', 'modified_at')


class ProductSeriesSerializer(s.ModelSerializer):
    class Meta:
        model = ProductSeries
        fields = ('id', 'model_series','created_at', 'modified_at')


class ManufacturerSerializer(s.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'manufacturer','created_at', 'modified_at')
