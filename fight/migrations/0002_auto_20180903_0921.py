# Generated by Django 2.0.6 on 2018-09-03 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='名字')),
                ('hp', models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='生命')),
                ('mp', models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='真气')),
                ('bandup', models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段上限')),
                ('banddown', models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段下限')),
                ('atk', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='外功')),
                ('mgk', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='内功')),
                ('agi', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='轻功')),
                ('avd', models.IntegerField(blank=True, max_length=100, null=True, verbose_name='回避率')),
                ('dex', models.IntegerField(blank=True, max_length=1000, null=True, verbose_name='会心率')),
                ('text', models.CharField(blank=True, max_length=65535, null=True, verbose_name='说明')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='avatar', verbose_name='头像')),
                ('defense', models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='防御_减伤')),
                ('vit', models.IntegerField(max_length=255, verbose_name='耐久')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fight.Armor', verbose_name='装备防具')),
            ],
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='名字')),
                ('hp', models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='生命')),
                ('mp', models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='真气')),
                ('bandup', models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段上限')),
                ('banddown', models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段下限')),
                ('atk', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='外功')),
                ('mgk', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='内功')),
                ('agi', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='轻功')),
                ('avd', models.IntegerField(blank=True, max_length=100, null=True, verbose_name='回避率')),
                ('dex', models.IntegerField(blank=True, max_length=1000, null=True, verbose_name='会心率')),
                ('text', models.CharField(blank=True, max_length=65535, null=True, verbose_name='说明')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='avatar', verbose_name='头像')),
                ('defense', models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='防御_减伤')),
                ('vit', models.IntegerField(max_length=255, verbose_name='耐久')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Equip',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='band_down',
            new_name='banddown',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='band_up',
            new_name='bandup',
        ),
        migrations.RemoveField(
            model_name='heart',
            name='band_down',
        ),
        migrations.RemoveField(
            model_name='heart',
            name='band_up',
        ),
        migrations.RemoveField(
            model_name='heart',
            name='id',
        ),
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='band_down',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='band_up',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='id',
        ),
        migrations.AddField(
            model_name='heart',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='heart',
            name='banddown',
            field=models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段下限'),
        ),
        migrations.AddField(
            model_name='heart',
            name='bandup',
            field=models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段上限'),
        ),
        migrations.AddField(
            model_name='heart',
            name='exp',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='武常经验'),
        ),
        migrations.AddField(
            model_name='role',
            name='defense',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='防御_减伤'),
        ),
        migrations.AddField(
            model_name='skill',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='skill',
            name='banddown',
            field=models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段下限'),
        ),
        migrations.AddField(
            model_name='skill',
            name='bandup',
            field=models.IntegerField(blank=True, max_length=64, null=True, verbose_name='波段上限'),
        ),
        migrations.AddField(
            model_name='skill',
            name='exp',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='武常经验'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='agi',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='atk',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='avd',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='dex',
            field=models.IntegerField(blank=True, max_length=1000, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='hp',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='mgk',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='mp',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='heart',
            name='name',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='role',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='agi',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='轻功'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='atk',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='外功'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='avd',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='回避率'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='dex',
            field=models.IntegerField(blank=True, max_length=1000, null=True, verbose_name='会心率'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='hp',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='生命'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='mgk',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='内功'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='mp',
            field=models.IntegerField(blank=True, max_length=65535, null=True, verbose_name='真气'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='名字'),
        ),
        migrations.AddField(
            model_name='weapons',
            name='equits',
            field=models.ManyToManyField(through='fight.Equit', to='fight.Role'),
        ),
        migrations.AddField(
            model_name='equit',
            name='heart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fight.Heart', verbose_name='装备心法'),
        ),
        migrations.AddField(
            model_name='equit',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fight.Role', verbose_name='角色名字'),
        ),
        migrations.AddField(
            model_name='equit',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fight.Skill', verbose_name='装备技能'),
        ),
        migrations.AddField(
            model_name='equit',
            name='weapons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fight.Weapons', verbose_name='装备武器'),
        ),
        migrations.AddField(
            model_name='armor',
            name='equits',
            field=models.ManyToManyField(through='fight.Equit', to='fight.Role'),
        ),
        migrations.AddField(
            model_name='heart',
            name='equits',
            field=models.ManyToManyField(through='fight.Equit', to='fight.Role'),
        ),
        migrations.AddField(
            model_name='skill',
            name='equits',
            field=models.ManyToManyField(through='fight.Equit', to='fight.Role'),
        ),
    ]