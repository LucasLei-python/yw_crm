# Generated by Django 2.0 on 2019-05-11 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20190511_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(limit_choices_to={'department__name': '项目部'}, on_delete=django.db.models.deletion.CASCADE, to='crm.UserInfo', verbose_name='咨询顾问'),
        ),
    ]
