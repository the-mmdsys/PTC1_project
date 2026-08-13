from django.db import models


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name="Category")
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True, verbose_name="Cover Image")
    content = models.TextField(verbose_name="Content")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    summary = models.TextField(blank=True, null=True, verbose_name="Summary")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Article"
    )
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    text = models.TextField(verbose_name="Text")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At") 

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.full_name} on {self.article.title}" 