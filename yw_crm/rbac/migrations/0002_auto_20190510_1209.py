# Generated by Django 2.0 on 2019-05-10 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='url别名'),
        ),
    ]