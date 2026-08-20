from core.serializers import DynamicFieldsModelSerializer
from ..models import OrderRequest, ContactWithUs

class OrderRequestSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = OrderRequest
        fields = (
            'id',
            'full_name',
            'company_name',
            'activity_area',
            'email',
            'phone_number',
            'message',
            'status',
            'created_at',
        )
        read_only_fields = ('id', 'status', 'created_at')


class ContactWithUsSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = (
            'id',
            'full_name',
            'email',
            'subject',
            'message',
            'status',
            'created_at',
        )
        read_only_fields = ('id', 'status', 'created_at')