from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    # 给管理后台增加显示的列
    list_display = ['name','password','email','sex']
    # 给管理后台增加可编辑的列
    list_editable = ['password','email','sex']

admin.site.register(models.User,  UserAdmin)