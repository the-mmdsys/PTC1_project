from django.db import models
from django.core.validators import FileExtensionValidator

class OrderRequest(models.Model):

    full_name     = models.CharField(max_length=100, verbose_name="Full Name")
    company_name  = models.CharField(max_length=150, blank=True, null=True, verbose_name="Company Name")
    activity_area = models.CharField(max_length=100, blank=True, null=True, verbose_name="Activity Area")
    email         = models.EmailField(verbose_name="Email")
    phone_number  = models.CharField(max_length=20, verbose_name="Phone Number") 
    massage          = models.TextField(verbose_name="Order Description")
    video_file    = models.FileField(
        upload_to ='order_requests/videos/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])],
        verbose_name="Video File"
    )
    is_reviewed   = models.BooleanField(default=False, verbose_name="Is Reviewed")
    created_at    = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name        = "Order Request"
        verbose_name_plural = "Order Requests" 
        ordering            = ['-created_at'] 

    def __str__(self):
        return f"Order from {self.full_name}"


class ContactWithUs(models.Model):
    full_name     = models.CharField(max_length=100, verbose_name="Full Name")
    email         = models.EmailField(verbose_name="Email")
    subject       = models.CharField(max_length=200, verbose_name="Subject") 
    message       = models.TextField(verbose_name="Message")
    is_read       = models.BooleanField(default=False, verbose_name="Is Read")
    created_at    = models.DateTimeField(auto_now_add=True, verbose_name="Created At") 

    class Meta:
        verbose_name        = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering            = ['-created_at'] 

    def __str__(self):
        return f"{self.subject} - {self.full_name}"