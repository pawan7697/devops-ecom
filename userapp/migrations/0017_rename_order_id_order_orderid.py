# Generated by Django 4.2.11 on 2024-05-14 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0016_remove_carts_order_carts_order_id_order_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='orderID',
        ),
    ]
