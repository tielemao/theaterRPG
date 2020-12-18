# Generated by Django 2.0.6 on 2018-09-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0002_auto_20180903_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armor',
            name='agi',
            field=models.IntegerField(blank=True, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='atk',
            field=models.IntegerField(blank=True, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='avd',
            field=models.IntegerField(blank=True, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='banddown',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段下限'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='bandup',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段上限'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='防御_减伤'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='dex',
            field=models.IntegerField(blank=True, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='hp',
            field=models.IntegerField(blank=True, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='mgk',
            field=models.IntegerField(blank=True, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='mp',
            field=models.IntegerField(blank=True, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='说明'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='vit',
            field=models.IntegerField(verbose_name='耐久'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='agi',
            field=models.IntegerField(blank=True, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='atk',
            field=models.IntegerField(blank=True, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='avd',
            field=models.IntegerField(blank=True, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='banddown',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段下限'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='bandup',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段上限'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='防御_减伤'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='dex',
            field=models.IntegerField(blank=True, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='exp',
            field=models.IntegerField(blank=True, null=True, verbose_name='武常经验'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='hp',
            field=models.IntegerField(blank=True, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='mgk',
            field=models.IntegerField(blank=True, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='mp',
            field=models.IntegerField(blank=True, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='说明'),
        ),
        migrations.AlterField(
            model_name='role',
            name='agi',
            field=models.IntegerField(blank=True, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='role',
            name='atk',
            field=models.IntegerField(blank=True, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='role',
            name='avd',
            field=models.IntegerField(blank=True, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='role',
            name='banddown',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段下限'),
        ),
        migrations.AlterField(
            model_name='role',
            name='bandup',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段上限'),
        ),
        migrations.AlterField(
            model_name='role',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='防御_减伤'),
        ),
        migrations.AlterField(
            model_name='role',
            name='dex',
            field=models.IntegerField(blank=True, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='role',
            name='hp',
            field=models.IntegerField(blank=True, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='role',
            name='mgk',
            field=models.IntegerField(blank=True, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='role',
            name='mp',
            field=models.IntegerField(blank=True, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='role',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='说明'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='agi',
            field=models.IntegerField(blank=True, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='atk',
            field=models.IntegerField(blank=True, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='avd',
            field=models.IntegerField(blank=True, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='banddown',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段下限'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='bandup',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段上限'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='防御_减伤'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='dex',
            field=models.IntegerField(blank=True, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='exp',
            field=models.IntegerField(blank=True, null=True, verbose_name='武常经验'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='hp',
            field=models.IntegerField(blank=True, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='mgk',
            field=models.IntegerField(blank=True, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='mp',
            field=models.IntegerField(blank=True, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='说明'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='agi',
            field=models.IntegerField(blank=True, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='atk',
            field=models.IntegerField(blank=True, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='avd',
            field=models.IntegerField(blank=True, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='banddown',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段下限'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='bandup',
            field=models.IntegerField(blank=True, null=True, verbose_name='波段上限'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='防御_减伤'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='dex',
            field=models.IntegerField(blank=True, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='hp',
            field=models.IntegerField(blank=True, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='mgk',
            field=models.IntegerField(blank=True, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='mp',
            field=models.IntegerField(blank=True, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='说明'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='vit',
            field=models.IntegerField(verbose_name='耐久'),
        ),
    ]
