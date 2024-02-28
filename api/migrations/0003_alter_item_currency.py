# Generated by Django 4.2.10 on 2024-02-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('eur', 'eur'), ('rub', 'rub')], max_length=3),
        ),
    ]
