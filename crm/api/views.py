from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from .serializers import OrderRequestSerializer, ContactWithUsSerializer
from . import services

class OrderRequestViewSet(mixins.CreateModelMixin, 
                          mixins.ListModelMixin, 
                          viewsets.GenericViewSet):

    http_method_names = ['post'] 
    serializer_class = OrderRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        order = services.create_order_request(**serializer.validated_data)
        
        result_serializer = self.get_serializer(order)
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)


class ContactWithUsViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = ContactWithUsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        contact = services.create_contact_message(**serializer.validated_data)
        
        result_serializer = self.get_serializer(contact)
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)