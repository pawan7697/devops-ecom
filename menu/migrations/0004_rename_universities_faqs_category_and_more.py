# Generated by Django 4.2.11 on 2024-05-06 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_size_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faqs',
            old_name='universities',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='universities',
            new_name='category',
        ),
    ]
