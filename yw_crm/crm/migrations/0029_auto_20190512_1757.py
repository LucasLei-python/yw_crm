# Generated by Django 2.0 on 2019-05-12 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0028_auto_20190512_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Procedure', verbose_name='上一个流程'),
        ),
        migrations.AlterField(
            model_name='productaudit',
            name='status',
            field=models.IntegerField(choices=[(1, '审核通过'), (2, '审核未通过')]),
        ),
    ]
