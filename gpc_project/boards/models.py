from django.db import models
from django.utils.timezone import now

# Create your models here.
class Article(models.Model):
    title = models.CharField('제목', max_length=126, null=False)
    content = models.TextField('내용',null=False)
    author = models.CharField('작성자', max_length=16, null=False)
    created_dt = models.DateTimeField('작성일', default=now)
    
    def __str__(self) -> str:
        return f'[{self.id}] {self.title}'