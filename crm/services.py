from .models import OrderRequest, ContactWithUs

def create_order_request(*, full_name, company_name, activity_area, email, phone_number, message) -> OrderRequest:
    order = OrderRequest.objects.create(
        full_name=full_name,
        company_name=company_name,
        activity_area=activity_area,
        email=email,
        phone_number=phone_number,
        message=message,
    )
    return order

def create_contact_message(*, full_name, email, subject, message) -> ContactWithUs:
    contact = ContactWithUs.objects.create(
        full_name=full_name,
        email=email,
        subject=subject,
        message=message
    )
    return contact