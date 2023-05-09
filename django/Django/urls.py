from django.contrib import admin
from django.urls import path, include
from main.views import ProductsAPIView
from main.views import InvoiceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'get_invoice', InvoiceViewSet, basename='get_invoice')

urlpatterns = [
    path('admin/', admin.site.urls),
    # API
    path('list/', ProductsAPIView.as_view()),
    path('', include(router.urls)),
]
