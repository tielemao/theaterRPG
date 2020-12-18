from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    """
    用于登录的用户表单
    """
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': '请输入用户名', }))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                             'placeholder': '请输入密码', }))
    captcha = CaptchaField(label="验证码")

class RegisterForm(forms.Form):
    """
    用于注册的用户表单
    """
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名',}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': '请输入密码',}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': '确认密码',}))
    email = forms.CharField(label="邮箱地址", widget=forms.EmailInput(attrs={'class':'form-control','placeholder': '请输入邮箱',}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label="验证码")
