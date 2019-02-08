from django.contrib import admin

from blog.models import Article


# 对模型进行管理(管理显示结构)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['writer', 'title', 'content', 'add_time', 'update_time', 'is_delete']
