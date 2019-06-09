# Generated by Django 2.0 on 2019-05-12 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_workshop_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Product', verbose_name='生产的产品'),
        ),
    ]
