from django.db import models

# Create your models here.

class news(models.Model):
    # 标题
    title = models.CharField(max_length=200)
    # 作者
    author = models.CharField(max_length=100)
    # 正文
    text = models.CharField(max_length=5000)
    # 原链接
    url = models.CharField(max_length=200)

    pub_time = models.DateTimeField('published')



