# Generated by Django 2.2.3 on 2019-07-13 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='事件执行人'),
        ),
        migrations.AddField(
            model_name='disk',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='asset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='parent_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_level', to='assets.BusinessUnit'),
        ),
        migrations.AddField(
            model_name='asset',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to=settings.AUTH_USER_MODEL, verbose_name='资产管理员'),
        ),
        migrations.AddField(
            model_name='asset',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_by', to=settings.AUTH_USER_MODEL, verbose_name='批准人'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.BusinessUnit', verbose_name='所属业务线'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.Contract', verbose_name='合同'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.IDC', verbose_name='所在机房'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.Manufacturer', verbose_name='制造商'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tags',
            field=models.ManyToManyField(blank=True, to='assets.Tag', verbose_name='标签'),
        ),
        migrations.AlterUniqueTogether(
            name='ram',
            unique_together={('asset', 'slot')},
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together={('asset', 'model', 'mac')},
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together={('asset', 'sn')},
        ),
    ]