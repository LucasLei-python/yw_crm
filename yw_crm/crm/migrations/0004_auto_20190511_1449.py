# Generated by Django 2.0 on 2019-05-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20190511_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.CharField(help_text='电话/微信等', max_length=31, verbose_name='联系方式'),
        ),
    ]
