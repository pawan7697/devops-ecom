# Generated by Django 4.2.11 on 2024-05-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_orderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='orderSatus',
            field=models.CharField(blank=True, default='Pending', max_length=255, null=True),
        ),
    ]
