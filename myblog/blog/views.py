from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from blog.forms import MessageBoardForm, UserForm, LoginForm
from blog.helper import set_password
from blog.models import Article, Label, Talk, MessageBoard, IndexPicture, User


class Login(View):
    """登陆"""

    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            # 合法
            user = form.cleaned_data['user']
            # 保存session
            request.session['ID'] = user.pk
            request.session['phone'] = user.phone
            # 登录成功跳转到主页
            return redirect('blog:主页')
        else:
            # 不合法
            return render(request, 'blog/login.html', context=form.errors)


class Reg(View):
    """注册"""

    def get(self, request):
        return render(request, 'blog/reg.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 验证数据合法性
        form = UserForm(data)
        if form.is_valid():
            # 保存数据库
            user = User()
            user.phone = form.cleaned_data.get('phone')
            user.password = set_password(form.cleaned_data.get('password'))
            user.save()
            # 跳转到登录
            return redirect('blog:登录')
        else:
            return render(request, 'blog/reg.html', context=form.errors)


class Index(View):
    """首页"""

    def get(self, request):
        # 操作数据
        pictures = IndexPicture.objects.filter(is_delete=False)
        # 获取文章按发布时间排序
        add_articles = Article.objects.filter(is_delete=False).order_by('-add_time')
        # 获取文章按阅读量排序
        read_articles = Article.objects.filter(is_delete=False).order_by('-read')
        # 获取标签
        labels = Label.objects.filter(is_delete=False)
        context = {
            'add_articles': add_articles,
            'read_articles': read_articles,
            'labels': labels,
            'pictures': pictures
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
