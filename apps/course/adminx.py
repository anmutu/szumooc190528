# _*_ coding :utf-8 _*_
__author__ = 'du'
__bolg__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2019/5/22 1:21'


import xadmin
from .models import Course, Chapter, Video


class CourseAdmin(object):
    """课程"""
    list_display = ['name', 'detail', 'category', 'tag', 'learn_num', 'collect_num', 'click_num']
    search_fields = ['name', 'detail', 'category', 'tag', 'learn_num', 'collect_num', 'click_num']
    list_filter = ['name', 'detail', 'category', 'tag', 'learn_num', 'collect_num', 'click_num']


class ChapterAdmin(object):
    """章节"""
    list_display = ['course', 'name', 'learn_minutes', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    """视频"""
    list_display = ['name', 'learn_minutes', 'add_time']
    search_fields = ['name', 'learn_minutes', 'add_time']
    list_filter = ['name', 'learn_minutes', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)
