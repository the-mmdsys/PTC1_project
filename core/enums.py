from django.db import models

class ActiveStatus(models.TextChoices):
    ACTIVE = 'active', 'فعال'
    INACTIVE = 'inactive', 'غیرفعال'

class ReviewStatus(models.TextChoices):
    PENDING = 'pending', 'در حال بررسی'
    REVIEWED = 'reviewed', 'بررسی شده'
    REJECTED = 'rejected', 'رد شده'

class ReadStatus(models.TextChoices):
    UNREAD = 'unread', 'خوانده نشده'
    READ = 'read', 'خوانده شده'

class ArticleStatus(models.TextChoices):
    DRAFT = 'draft', 'پیش‌نویس'
    PUBLISHED = 'published', 'منتشر شده'

class CommentStatus(models.TextChoices):
    PENDING = 'pending', 'در انتظار تأیید'
    APPROVED = 'approved', 'تأیید شده'
    REJECTED = 'rejected', 'رد شده'