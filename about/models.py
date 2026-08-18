from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

from core.models import OrderBaseModel  

class History(OrderBaseModel): 
    title = models.CharField(max_length=100, verbose_name="Title")
    achievement = models.TextField(verbose_name=_("Achievement"))
    year = models.CharField(max_length=50, verbose_name="Year")

    class Meta:
        verbose_name = _("History")
        verbose_name_plural = _("Histories")

    def __str__(self):
        return self.title


class TeamMember(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name=_("Name"))
    position = models.CharField(max_length=100, verbose_name=_("Role"))
    bio = models.TextField(verbose_name=_("Bio"),blank=True, null=True,)
    image = models.ImageField(upload_to='team_profiles/', blank=True, null=True, verbose_name=_("Profile Image"))

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.full_name
