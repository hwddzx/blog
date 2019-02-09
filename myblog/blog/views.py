from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from blog.forms import MessageBoardForm, UserForm
from blog.models import Article, Label, Talk, MessageBoard


class Login(View):
    """登陆"""

    def get(self, request):
        return render(request, 'blog/login.html')


class Reg(View):
    """注册"""

    def get(self, request):
        return render(request, 'blog/reg.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 操作数据
        form = UserForm(data)
        if form.is_valid():

            # 返回响应
            return HttpResponse('ok')
        else:
            return render(request, 'blog/reg.html', context=form.errors)


class Index(View):
    """首页"""

    def get(self, request):
        # 操作数据
        # 获取文章按发布时间排序
        add_articles = Article.objects.filter(is_delete=False).order_by('-add_time')
        # 获取文章按阅读量排序
        read_articles = Article.objects.filter(is_delete=False).order_by('-read')
        # 获取标签
        labels = Label.objects.filter(is_delete=False)
        context = {
            'add_articles': add_articles,
            'read_articles': read_articles,
            'labels': labels
        }
        return render(request, 'blog/index.html', context=context)


class Detail(View):
    """文章详情页"""

    def get(self, request, id):
        article = Article.objects.get(pk=id)
        # 获取文章按发布时间排序
        add_articles = Article.objects.filter(is_delete=False).order_by('-add_time')
        context = {
            'article': article,
            'add_articles': add_articles
        }
        return render(request, 'blog/article_detail.html', context=context)


class About(View):
    """关于"""

    def get(self, request):
        return render(request, 'blog/about.html')


class Acticle(View):
    """成长"""

    def get(self, request):
        articles = Article.objects.filter(is_delete=False)
        # 获取文章按发布时间排序
        add_articles = Article.objects.filter(is_delete=False).order_by('-add_time')
        context = {
            'add_articles': add_articles,
            'articles': articles
        }
        return render(request, 'blog/article.html', context=context)


class Comment(View):
    """留言"""

    def get(self, request):
        messages = MessageBoard.objects.all().order_by('-add_time')
        context = {
            'messages': messages
        }
        return render(request, 'blog/comment.html', context=context)

    def post(self, requset):
        # 接收参数
        data = requset.POST
        form = MessageBoardForm(data)
        # 判断合法性
        if form.is_valid():
            content = data['content']
            # 操作数据库
            MessageBoard.objects.create(content=content)
            return redirect('blog:留言')
        else:
            # 不合法,返回错误提示
            errors = form.errors
            messages = MessageBoard.objects.all().order_by('-add_time')
            context = {
                'errors': errors,
                'messages': messages
            }
            return render(requset, 'blog/comment.html', context=context)


class MoodList(View):
    """说说"""

    def get(self, request):
        # 获取说说数据
        talks = Talk.objects.filter(is_delete=False)
        context = {
            'talks': talks
        }
        return render(request, 'blog/moodList.html', context=context)
