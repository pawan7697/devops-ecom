# Generated by Django 4.2.11 on 2024-05-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0018_remove_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='order_id',
        ),
        migrations.AddField(
            model_name='carts',
            name='orderID',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
