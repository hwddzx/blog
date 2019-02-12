from django.core.validators import RegexValidator
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    writer = models.CharField(max_length=20, verbose_name='发布者')
    title = models.CharField(max_length=50, verbose_name='标题')
    content = RichTextUploadingField(verbose_name='内容')
    read = models.SmallIntegerField(default=0, verbose_name='阅读量')
    comment = models.SmallIntegerField(default=0, verbose_name='评论数')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Label(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名')
    article = models.ManyToManyField(to='Article', verbose_name='文章')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Talk(models.Model):
    """说说"""
    content = models.CharField(max_length=255, verbose_name='说说')
    picture = models.ImageField(upload_to='talk/%Y%m/%d', verbose_name='说说图片', null=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '说说管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class IndexPicture(models.Model):
    """首页轮播"""
    title = models.CharField(max_length=20, verbose_name='图片描述')
    picture = models.ImageField(upload_to='home/%Y%m', verbose_name='首页轮播图片')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '首页轮播管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MessageBoard(models.Model):
    content = models.CharField(max_length=255, verbose_name='留言内容')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    class Meta:
        verbose_name = '留言板管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class User(models.Model):
    phone = models.CharField(max_length=11,
                             verbose_name='手机号',
                             validators=[
                                 RegexValidator(r'^1[3-9]\d{9}$', "手机号码格式错误!")
                             ])
    password = models.CharField(max_length=32, verbose_name='密码')
    integral = models.SmallIntegerField(verbose_name='积分', default=0)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone
