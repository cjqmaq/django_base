from django.db import models

# Create your models here.

class Account(models.Model):
    # 用户名
    user_name = models.CharField(max_length=200)

    # 密码
    pass_word = models.CharField(max_length=200)

    # 最近登录时间
    last_login_time = models.DateTimeField('published')

class Blog(models.Model):
    '''
    日志表
    '''
    # 标题
    title = models.CharField(max_length=200)

    # 发布时间
    pub_date = models.DateTimeField('published')

    # 正文
    content = models.CharField(max_length=2000)

    account = models.ForeignKey(Account,on_delete=models.CASCADE)

    key_words = models.CharField(max_length=500)

class Keywords(models.Model):
    key_word = models.CharField(max_length=50)


class BlogKeywords(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    key_word = models.ForeignKey(Keywords,on_delete=models.CASCADE)


class Comment(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField('published')
    approval = models.IntegerField(default=0)
    oppose = models.IntegerField(default=0)



