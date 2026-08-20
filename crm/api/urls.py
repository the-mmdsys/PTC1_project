from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderRequestViewSet, ContactWithUsViewSet

app_name = 'crm'

router = DefaultRouter()
router.register(r'order-request', OrderRequestViewSet, basename='order-request')
router.register(r'contact-us', ContactWithUsViewSet, basename='contact-us')

urlpatterns = [
    path('', include(router.urls)),
]