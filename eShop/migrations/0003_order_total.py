# Generated by Django 5.0.1 on 2024-01-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eShop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]
