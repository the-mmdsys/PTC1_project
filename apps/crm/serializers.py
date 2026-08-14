from rest_framework import serializers
from .models import OrderRequest, ContactWithUs


class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRequest
        fields = (
            'full_name',
            'company_name',
            'activity_area',
            'email',
            'phone_number',
            'massage',
            'video_file',
        )


class ContactWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = (
            'full_name',
            'email',
            'subject',
            'message',
        )