from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel

class History(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Title")
    achievement = models.TextField(verbose_name=_("Achievement"))
    date = models.DateField(verbose_name=_("Date"))

    class Meta:
        verbose_name = _("History")
        verbose_name_plural = _("Histories")

    def __str__(self):
        return self.title


class TeamMember(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name=_("Name"))
    position = models.CharField(max_length=100, verbose_name=_("Role"))
    bio = models.TextField(verbose_name=_("Bio"))
    image = models.ImageField(upload_to='team_profiles/', blank=True, null=True, verbose_name=_("Profile Image"))

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.full_name