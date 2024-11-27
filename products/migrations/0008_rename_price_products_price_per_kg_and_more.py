# Generated by Django 5.1.2 on 2024-11-21 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_products_deals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='price_per_kg',
        ),
        migrations.AddField(
            model_name='products',
            name='is_piece_based',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.products')),
            ],
        ),
    ]