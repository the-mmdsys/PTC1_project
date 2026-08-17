from django.db import models
from core.models import BaseModel
from core.enums import ArticleStatus, CommentStatus
from django.utils.translation import gettext_lazy as _


class Article(BaseModel):
    title       = models.CharField(max_length=200, verbose_name=_("Title"))
    slug        = models.SlugField(max_length=200, unique=True, verbose_name=_("Slug"))
    category    = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Category"))
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True, verbose_name=_("Cover Image"))
    content     = models.TextField(verbose_name=_("Content"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    summary     = models.TextField(blank=True, null=True, verbose_name=_("Summary"))
    
    status = models.CharField(
        max_length=20, 
        choices=ArticleStatus.choices, 
        default=ArticleStatus.PUBLISHED, 
        verbose_name=_("Status")
    )

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title


class Comment(BaseModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Article")
    )
    full_name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    text      = models.TextField(verbose_name="Text")
    
    status = models.CharField(
        max_length=20, 
        choices=CommentStatus.choices, 
        default=CommentStatus.PENDING, 
        verbose_name=_("Status")
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"Comment by {self.full_name} on {self.article.title}"