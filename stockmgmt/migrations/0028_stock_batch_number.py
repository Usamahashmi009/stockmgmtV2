# Generated by Django 4.2.6 on 2023-11-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0027_remove_costofgoodssold_cost_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='batch_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]