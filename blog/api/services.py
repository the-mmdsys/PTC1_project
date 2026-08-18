from ..models import Article, Comment

def create_comment(*, article: Article, full_name: str, text: str) -> Comment:
    comment = Comment.objects.create(
        article=article,
        full_name=full_name,
        text=text
    )
    return comment