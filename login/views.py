from django.shortcuts import render, redirect, reverse
from . import models, forms
import hashlib


def hash_code(s, salt='txdx'):
    """
    简单加盐,密文保存密码
    """
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return render(request, 'login/index.html')

def login(request):
    """
    登录
    :param request:
    :return:
    """
    # 如己有登录状态，则不再重复登录
    if request.session.get('is_login',None):
        return redirect("/index/")

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    # 数据库密码和哈希后的用户密码相比较一致
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def logout(request):
    """
    注销
    :param request:
    :return:
    """
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就用不着清空session
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")

def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.session.get('is_login',None):
        # 登录状态一般不允许注册，也可以修改成允许
        return redirect("/index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1) # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面

    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())



