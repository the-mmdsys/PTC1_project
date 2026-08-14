from django.db import models

class History(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    achievement = models.TextField(verbose_name="Achievement")
    date = models.DateField(verbose_name="Date")

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"
        ordering = ['date']

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Name")
    position = models.CharField(max_length=100, verbose_name="Role")
    bio = models.TextField(verbose_name="Bio")
    image = models.ImageField(upload_to='team_profiles/', blank=True, null=True, verbose_name="Profile Image")

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name



