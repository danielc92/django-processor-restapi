from django.contrib import admin
from .models import Processors, Manufacturer, ProductSeries

# Register your models here.
admin.site.register(Processors)
admin.site.register(Manufacturer)
admin.site.register(ProductSeries)