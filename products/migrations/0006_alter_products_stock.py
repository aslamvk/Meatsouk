# Generated by Django 5.1.2 on 2024-11-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
