# Generated by Django 4.2.7 on 2023-11-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_currencyexchangeinfo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyexchangeinfo',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
