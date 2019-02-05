from django.conf.urls import url

from blog.views import Index, Detail

urlpatterns = [
    url(r'^$', Index.as_view(), name='主页'),
    url(r'^detail$', Detail.as_view(), name='文章详情'),
]
