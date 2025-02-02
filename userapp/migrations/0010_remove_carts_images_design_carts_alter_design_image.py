# Generated by Django 4.2.11 on 2024-05-14 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_remove_design_cart_carts_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='images',
        ),
        migrations.AddField(
            model_name='design',
            name='carts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designs', to='userapp.carts'),
        ),
        migrations.AlterField(
            model_name='design',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='designs_img'),
        ),
    ]
