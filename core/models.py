from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


class OrderBaseModel(BaseModel):
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        abstract = True
        ordering = ['order']