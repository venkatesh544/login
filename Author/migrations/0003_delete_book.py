# Generated by Django 3.0.7 on 2021-08-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
