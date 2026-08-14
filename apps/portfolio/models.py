from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    active_status = models.BooleanField(default=True, verbose_name="Active Status")
    logo = models.ImageField(upload_to='category_logos/', blank=True, null=True, verbose_name="Logo")
    order = models.IntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['order']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Project Title")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="Slug (URL)")
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
        verbose_name="Created By"
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Project"
    )
    image = models.ImageField(upload_to='project_images/gallery/', verbose_name="Image")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Gallery"

    def __str__(self):
        return f"Image for {self.project.title}"