# Generated by Django 3.0.7 on 2021-07-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0009_auto_20210729_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]