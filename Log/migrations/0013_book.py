# Generated by Django 3.0.7 on 2021-08-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0012_auto_20210730_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs')),
            ],
        ),
    ]
