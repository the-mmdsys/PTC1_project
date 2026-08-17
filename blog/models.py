from django.db import models
from core.models import BaseModel, OrderBaseModel
from core.enums import ArticleStatus, CommentStatus
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class Category(OrderBaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, blank=True, verbose_name=_("Slug"))

    class Meta(OrderBaseModel.Meta):
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class Article(BaseModel):
    class Language(models.TextChoices):
        PERSIAN = 'fa', _('Persian')
        ENGLISH = 'en', _('English')
        ARABIC = 'ar', _('Arabic')

    title       = models.CharField(max_length=200, verbose_name=_("Title"))
    slug        = models.SlugField(max_length=200, allow_unicode=True, unique=True, blank=True, verbose_name=_("Slug"))
    category    = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
        verbose_name=_("Category")
    )
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.PERSIAN,
        verbose_name=_("Language")
    )
    cover_image = models.ImageField(upload_to='article_covers/', blank=True, null=True, verbose_name=_("Cover Image"))
    content     = RichTextUploadingField(verbose_name=_("Content"))
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


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
