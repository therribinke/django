# Generated by Django 4.2.20 on 2025-03-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_ticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
