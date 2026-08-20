from django.db import models
from django.core.validators import RegexValidator
from core.models import BaseModel
from core.enums import ReviewStatus, ReadStatus
from django.utils.translation import gettext_lazy as _

class OrderRequest(BaseModel):
    full_name     = models.CharField(max_length=100, verbose_name=_("Full Name"))
    company_name  = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("Company Name"))
    activity_area = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Activity Area"))
    email         = models.EmailField(verbose_name=_("Email"))
    phone_number  = models.CharField(max_length=20, verbose_name=_("Phone Number"), validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]) 
    message       = models.TextField(verbose_name=_("Order Description"))
    
    
    
    status = models.CharField(
        max_length=20, 
        choices=ReviewStatus.choices, 
        default=ReviewStatus.PENDING,
        verbose_name=_("Review Status")
    )

    class Meta:
        verbose_name        = _("Order Request")
        verbose_name_plural = _("Order Requests") 

    def __str__(self):
        return f"Order from {self.full_name}"


class ContactWithUs(BaseModel):
    full_name     = models.CharField(max_length=100, verbose_name=_("Full Name"))
    email         = models.EmailField(verbose_name=_("Email"))
    subject       = models.CharField(max_length=200, verbose_name=_("Subject")) 
    message       = models.TextField(verbose_name=_("Message"))
    
    status = models.CharField(
        max_length=20,
        choices=ReadStatus.choices,
        default=ReadStatus.UNREAD,
        verbose_name=_("Read Status")
    )

    class Meta:
        verbose_name        = _("Contact Message")
        verbose_name_plural = _("Contact Messages")

    def __str__(self):
        return f"{self.subject} - {self.full_name}"
