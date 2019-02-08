from django.db import models


class Article(models.Model):
    writer = models.CharField(max_length=20, verbose_name='发布者')
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
