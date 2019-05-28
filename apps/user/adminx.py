# _*_ coding :utf-8 _*_
__author__ = 'du'
__bolg__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2019/5/22 1:22'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    """视频"""
    list_display = ['nick_name', 'birthday', 'gender', 'address', 'mobile']
    search_fields = ['nick_name', 'birthday', 'gender', 'address', 'mobile']
    list_filter = ['nick_name', 'birthday', 'gender', 'address', 'mobile']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "深圳大学慕课网管理系统"
    site_footer = "深圳大学慕课网"
    menu_style = "accordion"


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
