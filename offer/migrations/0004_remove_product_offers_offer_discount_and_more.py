# Generated by Django 5.1.2 on 2024-12-02 05:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_rename_offer_price_category_offers_offer_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_offers',
            name='offer_discount',
        ),
        migrations.AddField(
            model_name='product_offers',
            name='offer_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)]),
        ),
    ]
