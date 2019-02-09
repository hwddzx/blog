from django.conf.urls import url

from blog.views import Index, Detail, About, Acticle, Comment, MoodList, Login, Reg

urlpatterns = [
    url(r'^$', Index.as_view(), name='主页'),
    url(r'^detail/(\d+)/$', Detail.as_view(), name='文章详情'),
    url(r'^about', About.as_view(), name='关于'),
    url(r'^acticle', Acticle.as_view(), name='成长'),
    url(r'^comment', Comment.as_view(), name='留言'),
    url(r'^moodList', MoodList.as_view(), name='说说'),
    url(r'^login', Login.as_view(), name='登录'),
    url(r'^reg', Reg.as_view(), name='注册'),
]
