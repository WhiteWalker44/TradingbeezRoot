# Generated by Django 4.2.7 on 2023-11-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_currencyexchangeinfo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyexchangeinfo',
            name='price',
            field=models.PositiveIntegerField(blank=True, max_length=5, null=True),
        ),
    ]
