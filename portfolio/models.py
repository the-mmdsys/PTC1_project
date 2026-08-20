from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel, OrderBaseModel
from core.enums import ActiveStatus
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class CustomUser(AbstractUser):
    pass

class Category(OrderBaseModel):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    
    active_status = models.CharField(
        max_length=20, 
        choices=ActiveStatus.choices, 
        default=ActiveStatus.ACTIVE, 
        verbose_name=_("Active Status")
    )
    
    logo = models.ImageField(upload_to='category_logos/', blank=True, null=True, verbose_name=_("Logo"))

    class Meta(OrderBaseModel.Meta):
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Project(OrderBaseModel):
    title = models.CharField(max_length=100, verbose_name="Project Title")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, blank=True, verbose_name="Slug (URL)")
    description = models.TextField(verbose_name="Description")
    cover_image = models.ImageField(upload_to='project_images/covers/', blank=True, null=True, verbose_name="Cover Image")
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Category"
    )

    created_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='created_projects',
        verbose_name=_("Created By")
    )

    class Meta(OrderBaseModel.Meta):
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class ProjectImage(OrderBaseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Project")
    )
    image = models.ImageField(upload_to='project_images/gallery/', verbose_name=_("Image"))
    
    is_active = models.CharField(
        max_length=20, 
        choices=ActiveStatus.choices, 
        default=ActiveStatus.ACTIVE, 
        verbose_name=_("Active")
    )

    class Meta(OrderBaseModel.Meta):
        verbose_name = _("Project Image")
        verbose_name_plural = _("Project Gallery")

    def __str__(self):
        return f"Image for {self.project.title}"
