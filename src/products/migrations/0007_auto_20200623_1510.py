# Generated by Django 2.1.5 on 2020-06-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200622_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]
