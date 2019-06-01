from django.contrib.auth.hashers import make_password
import django.http
from django.http import HttpResponse
from django.views.generic.base import View
from .form import LoginForm, RegisterForm, UserInfoForm, UploadImageForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import UserProfile
from utils.mixin_utils import LoginRequiredMixin
import json
import django.http.request


# 用户登录的view
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
               login(request, user)
               return django.http.HttpResponseRedirect("/course/info/1")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


# 注册用户的view
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("user", "")
            if UserProfile.objects.filter(username=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class UserinfoView(LoginRequiredMixin,View):
    """
        用户个人信息
        """

    def get(self, request):
        return render(request, 'usercenter-info.html', {})

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return django.http.HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return django.http.HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    """
    上传头像
    """
    def post(self, request):
        portrait_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if portrait_form.is_valid():
            portrait_form.save()
            return django.http.HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return django.http.HttpResponse('{"status":"fail"}', content_type='application/json')
