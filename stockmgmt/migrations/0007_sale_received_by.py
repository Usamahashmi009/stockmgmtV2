# Generated by Django 4.2.6 on 2023-10-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0006_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='received_by',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
