from rest_framework import serializers as s
from .models import Processors, Manufacturer, ProductSeries

class ProcessorsSerializer(s.ModelSerializer):
    class Meta:
        model = Processors
        fields = ('id','core_count','thread_count', 'tdp_watts', 'model_name', 'model_series',
        'manufacturer', 'rrp_usd', 'base_clock', 'turbo_clock', 'created_at', 'modified_at')


"""
class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manufacturer

class ProductSeries(models.Model):
    model_series = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model_series

# Create your models here.
class Processors(models.Model):
    core_count = models.IntegerField()
    thread_count = models.IntegerField()
    tdp_watts = models.IntegerField()
    model_name =  models.CharField(max_length=255)
    model_series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    rrp_usd = models.DecimalField(max_digits=10, decimal_places=2)
    base_clock = models.DecimalField(max_digits=10, decimal_places=2)
    turbo_clock = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
"""