# Generated by Django 5.0.7 on 2024-10-21 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]