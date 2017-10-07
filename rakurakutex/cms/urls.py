from django.conf.urls import url
from cms import views
from django.contrib.auth.views import login,logout
from django.contrib.auth import views as auth_views
import django.contrib.auth.views

urlpatterns = [
    # 書籍
    url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除
    # 感想
    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>\d+)/$', views.impression_edit, name='impression_add'),        # 登録
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),   # 削除
    #url(r'^login/$',django.contrib.auth.views.login,{'template_name': 'cms/login.html',},name='login'),
    #url(r'^logout/$',django.contrib.auth.views.logout,{'template_name': 'cms/logged_out.html',},name='logout'),
    url(r'^login/$', login,{'template_name': 'cms/login.html'},name='login'),
    url(r'^logout/$', logout,{'template_name': 'cms/logged_out.html',}, name='logout')
]
