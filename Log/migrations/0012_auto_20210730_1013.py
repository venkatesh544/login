# Generated by Django 3.0.7 on 2021-07-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0011_auto_20210730_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
