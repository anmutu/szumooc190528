"""szumooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from user.views import RegisterView,LoginView
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    # 用户注册
    url('^register/$', RegisterView.as_view(), name="register"),

    # 用户登录
    url('^login/$', LoginView.as_view(), name="login"),

    # 验证码需要用到
    url(r'^captcha/', include('captcha.urls')),

    # 课程相关url配置(分发到course下的urls.py里)
    url(r'^course/', include(('course.urls', 'course'), namespace="course")),

    # 用户相关url配置(分发到user下的urls.py里)
    url(r'^user/', include(('user.urls', 'user'), namespace="user")),
]
