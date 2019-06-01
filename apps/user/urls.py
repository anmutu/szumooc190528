# _*_ coding :utf-8 _*_
__author__ = 'du'
__bolg__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2019/5/31 8:11'

from django.conf.urls import url
from user.views import UserinfoView, UploadImageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
]