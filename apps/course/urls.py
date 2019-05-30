# _*_ coding :utf-8 _*_
__author__ = 'du'
__bolg__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2019/5/23 19:26'

from django.conf.urls import url, include
from .views import ChapterListView, VideoPlayView, GetCommentsView, AddCommentView

urlpatterns = [

    # 课程章节列表信息
    url(r'^info/(?P<course_id>\d+)/$', ChapterListView.as_view(), name="course_info"),

    # 视频播放
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video-play"),

    # 得到课程评论信息
    url(r'^comment/(?P<course_id>\d+)/$', GetCommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name="add_comment"),
]
