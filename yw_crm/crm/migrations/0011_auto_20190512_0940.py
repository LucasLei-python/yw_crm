# Generated by Django 2.0 on 2019-05-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20190512_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='confirm_date',
            field=models.DateField(blank=True, null=True, verbose_name='确认日期'),
        ),
    ]
