from django.contrib import admin

from blog.models import Article, Label, Talk, MessageBoard, IndexPicture


# 对模型进行管理(管理显示结构)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 10
    # 指定显示的列
    list_display = ['writer', 'title', 'read', 'comment', 'add_time', 'update_time', 'is_delete']


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'add_time', 'update_time', 'is_delete']


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['content', 'picture', 'add_time', 'is_delete']


@admin.register(MessageBoard)
class TalkAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['content', 'add_time']


@admin.register(IndexPicture)
class IndexPictureAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['title', 'picture', 'add_time', 'is_delete']
