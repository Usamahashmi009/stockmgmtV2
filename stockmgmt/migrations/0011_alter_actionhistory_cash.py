# Generated by Django 4.2.6 on 2023-11-02 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0010_actionhistory_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionhistory',
            name='cash',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='stockmgmt.stock'),
            preserve_default=False,
        ),
    ]
