from django.db import models


class Img(models.Model):
    img_url = models.ImageField(upload_to='img')


class Panel(models.Model):
    """
    人物基础属性面板，做为一个抽象类让下面的表继承
    """
    name = models.CharField(verbose_name="名字", primary_key=True, max_length=32, unique=True)
    hp = models.IntegerField(verbose_name="生命", blank=True, null=True)
    mp = models.IntegerField(verbose_name="真气", blank=True, null=True)
    bandup = models.IntegerField(verbose_name="波段上限", blank=True, null=True)
    banddown = models.IntegerField(verbose_name="波段下限", blank=True, null=True)
    atk = models.IntegerField(verbose_name="功力", blank=True, null=True)
    str = models.IntegerField(verbose_name="外功", blank=True, null=True)
    mgk = models.IntegerField(verbose_name="内功", blank=True, null=True)
    agi = models.IntegerField(verbose_name="轻功", blank=True, null=True)
    avd = models.IntegerField(verbose_name="回避率", blank=True, null=True)
    dex = models.IntegerField(verbose_name="会心率",  blank=True, null=True)
    text = models.CharField(verbose_name="说明", max_length=256, blank=True, null=True)
    avatar = models.FileField(verbose_name="头像", upload_to='img', blank=True, null=True)
    defense = models.IntegerField(verbose_name="防御_减伤", blank=True, null=True)

    def __str__(self):
        return self.name

    # 设置成为抽象类
    class Meta:
        abstract = True


class Role(Panel):
    """
    角色表
    """

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "角色表"
        verbose_name_plural = "角色表"

class Weapons(Panel):
    """
    武器表
    """

    vit = models.IntegerField(verbose_name="耐久")
    equits = models.ManyToManyField(Role, through="Equit")

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "武器表"
        verbose_name_plural = "武器表"

class Armor(Panel):
    """
    防具表
    """

    vit = models.IntegerField(verbose_name="耐久")
    equits = models.ManyToManyField(Role, through="Equit")

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "防具表"
        verbose_name_plural = "防具表"


class Spirit(Panel):
    """
    灵器表
    """
    psy = models.IntegerField(verbose_name="灵力")
    equits = models.ManyToManyField(Role, through="Equit")

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "灵力表"
        verbose_name_plural = "灵力表"


class Skill(Panel):
    """
    武学，招式表
    """

    exp = models.IntegerField(verbose_name="武常经验", blank=True, null=True)
    equits = models.ManyToManyField(Role, through="Equit")

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "技能表"
        verbose_name_plural = "技能表"


class Heart(Panel):
    """
    内功心法表
    """

    exp = models.IntegerField(verbose_name="武常经验", blank=True, null=True)
    equits = models.ManyToManyField(Role, through="Equit")

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "心法表"
        verbose_name_plural = "心法表"


class Equit(models.Model):
    """
    角色装备表
    """
    role = models.OneToOneField(to=Role, verbose_name="角色名字", on_delete=models.CASCADE)
    weapons = models.ForeignKey(to=Weapons, verbose_name="装备武器", on_delete=models.CASCADE, blank=True, null=True)
    armor = models.ForeignKey(to=Armor, verbose_name="装备防具", on_delete=models.CASCADE, blank=True, null=True)
    skill = models.ForeignKey(to=Skill, verbose_name="装备技能", on_delete=models.CASCADE, blank=True, null=True)
    heart = models.ForeignKey(to=Heart, verbose_name="装备心法", on_delete=models.CASCADE, blank=True, null=True)
    spirit = models.ForeignKey(to=Spirit, verbose_name="装备灵器", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        # 指定在admin管理界面显示中文
        verbose_name = "角色装备表"
        verbose_name_plural = "角色装备表"