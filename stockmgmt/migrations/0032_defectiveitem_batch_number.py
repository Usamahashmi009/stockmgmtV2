# Generated by Django 4.2.6 on 2023-11-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0031_remove_sale_batch_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='defectiveitem',
            name='batch_number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
