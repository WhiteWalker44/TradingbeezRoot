# Generated by Django 4.2.7 on 2023-11-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiatcurrency',
            name='price',
        ),
        migrations.AddField(
            model_name='currencyexchangeinfo',
            name='price',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
