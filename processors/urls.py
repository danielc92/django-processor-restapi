from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('processors', views.ProcessorView)
router.register('manufacturers', views.ManufacturerView)
router.register('product-series', views.ProductSeriesView)


urlpatterns = [
    path('', include(router.urls))
]