# Generated by Django 4.2.6 on 2023-12-05 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0060_remove_itemsmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='stockmgmt.category'),
            preserve_default=False,
        ),
    ]
