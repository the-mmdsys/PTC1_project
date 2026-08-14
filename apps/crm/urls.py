from django.urls import path
from .views import OrderRequestCreateView, ContactWithUsCreateView

app_name = 'crm'

urlpatterns = [
    path('order-request/', OrderRequestCreateView.as_view(), name='order-request-create'),
    path('contact-us/', ContactWithUsCreateView.as_view(), name='contact-us-create'),
]
