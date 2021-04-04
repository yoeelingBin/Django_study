"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # 格式 : url(regex正则表达式, view视图函数, kwargs=None传入参数, name=None url的名字)
    url(r'^$', views.home, name='home'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^(?P<username>[\w.@+-]+/$', views.user_profile, name='user_profile'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # url(r'^about/company/$', views.about_company, name='about_company'),
    # url(r'^about/author/$', views.about_author, name='about_author'),
    # url(r'^about/author/vitor$', views.about_vitor, name='about_vitor'),
    # url(r'^about/author/erica$', views.about_erica, name='about_erica'),
    # url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),

    url(r'^admin/', admin.site.urls),
]
