# Generated by Django 4.2.8 on 2023-12-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userwallet_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='pin',
            field=models.CharField(max_length=4),
        ),
    ]
