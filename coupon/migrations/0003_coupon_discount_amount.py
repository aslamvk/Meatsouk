# Generated by Django 5.1.2 on 2024-11-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_remove_coupon_used_remove_coupon_user_usercoupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]