# Generated by Django 5.0.7 on 2024-11-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_payment_status_alter_order_payment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Failure', 'Failure')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('COD', 'Cash on Delivery'), ('RazorPay', 'Razor Pay'), ('Wallet', 'Wallet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('order pending', 'order pending'), ('order confirmed', 'order confirmed'), ('shipped', 'shipped'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered'), ('cancelled', 'cancelled'), ('requested return', 'requested return'), ('approve return', 'approve return'), ('reject return', 'reject return')], default='Order Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='subtotal_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]