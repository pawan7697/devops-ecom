# Generated by Django 4.2.11 on 2024-05-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='price',
            field=models.IntegerField(),
        ),
    ]
