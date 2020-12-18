from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return render(request, 'fight/index.html')

def role_list(request):
    roles = models.Role.objects.all()
    return render(request, 'fight/role_list.html', {'roles':roles})

def uploadImg(request):
    # 上传图片
    if request.method == "POST":
        img = models.Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'fight/imgupload.html')

def showImg(request):
    imgs = models.Img.objects.all()
    # 从数据库中取出所有的图片路径
    context = {
        'imgs': imgs
    }
    return render(request, 'fight/showImg.html', context)

def role_vs(request):
    """
    模拟角色战斗
    :param request:
    :return:
    """

    return render(request, 'fight/role_vs.html')