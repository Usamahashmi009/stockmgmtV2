# Generated by Django 4.2.6 on 2023-11-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0035_remove_stock_account_recieveable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionhistory',
            name='cash_hand',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
