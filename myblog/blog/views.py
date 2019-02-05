from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View


class Index(View):
    """首页"""

    def get(self, request):
        return render(request, 'blog/index.html')


class Detail(View):
    """文章详情页"""

    def get(self, request):
        return render(request, 'blog/article_detail.html')
