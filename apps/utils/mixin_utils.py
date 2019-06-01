# _*_ coding :utf-8 _*_
__author__ = 'du'
__bolg__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2019/5/31 8:17'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
