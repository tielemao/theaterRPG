import random
import numpy as np
import math
from matplotlib import pyplot as plt
from django.db import models
# pyplot用于生成直方图


class People(models.Models):
    """
    武林人物类
    """
    name = models.CharField(verbose_name="名字", primary_key=True, max_length=32, unique=True)
    hp = models.IntegerField(verbose_name="生命", blank=True, null=True)
    bandup = models.IntegerField(verbose_name="波段上限", blank=True, null=True)
    banddown = models.IntegerField(verbose_name="波段下限", blank=True, null=True)
    atk = models.IntegerField(verbose_name="功力", blank=True, null=True)

    # mp = models.IntegerField(verbose_name="真气", blank=True, null=True)
    # str = models.IntegerField(verbose_name="外功", blank=True, null=True)
    # mgk = models.IntegerField(verbose_name="内功", blank=True, null=True)
    # agi = models.IntegerField(verbose_name="轻功", blank=True, null=True)
    # avd = models.IntegerField(verbose_name="回避率", blank=True, null=True)
    # dex = models.IntegerField(verbose_name="会心率",  blank=True, null=True)
    # text = models.CharField(verbose_name="说明", max_length=256, blank=True, null=True)
    # avatar = models.FileField(verbose_name="头像", upload_to='img', blank=True, null=True)
    # defense = models.IntegerField(verbose_name="防御_减伤", blank=True, null=True)

    def __str__(self):
        return self.name

    # 设置成为抽象类，不会生成数据库表
    class Meta:
        abstract = True


class Hero(People):

    pass

xiaoming = Hero("小明")

print(xiaoming)