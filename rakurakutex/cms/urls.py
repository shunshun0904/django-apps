from django.conf.urls import url
from cms import views
from django.contrib.auth import views as auth_views
import django.contrib.auth.views

urlpatterns = [
    # 書籍
    url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^index/$', views.index_list, name='book_list'),   # 一覧
    url(r'^book/mypage/$', views.mypage_list, name='mypage'),   # 一覧

    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>\d+)/$', views.impression_edit, name='impression_add'),        # 登録
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),   # 削除

]
