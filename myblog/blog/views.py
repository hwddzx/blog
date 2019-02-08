from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from blog.models import Article


class Index(View):
    """首页"""

    def get(self, request):
        # 操作数据
        articles = Article.objects.filter(is_delete=False).order_by('add_time')
        context = {
            'articles': articles
        }
        return render(request, 'blog/index.html', context=context)


class Detail(View):
    """文章详情页"""

    def get(self, request):
        return render(request, 'blog/article_detail.html')


class About(View):
    """关于"""

    def get(self, request):
        return render(request, 'blog/about.html')


class Acticle(View):
    """成长"""

    def get(self, request):
        return render(request, 'blog/article.html')


class Comment(View):
    """留言"""

    def get(self, request):
        return render(request, 'blog/comment.html')


class MoodList(View):
    """说说"""

    def get(self, request):
        return render(request, 'blog/moodList.html')
