# Generated by Django 4.2.6 on 2023-11-01 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0009_addcash_stock_addcash'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionhistory',
            name='cash',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmt.stock'),
        ),
    ]
