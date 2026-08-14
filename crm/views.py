from rest_framework import generics
from .models import OrderRequest, ContactWithUs
from .serializers import OrderRequestSerializer, ContactWithUsSerializer

class OrderRequestCreateView(generics.CreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer


class ContactWithUsCreateView(generics.CreateAPIView):
    queryset = ContactWithUs.objects.all()
    serializer_class = ContactWithUsSerializer