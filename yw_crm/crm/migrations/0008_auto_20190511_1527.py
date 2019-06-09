# Generated by Django 2.0 on 2019-05-11 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20190511_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='referral_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral', to='crm.Customer', verbose_name='自己内部顾客介绍'),
        ),
    ]