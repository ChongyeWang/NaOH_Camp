# Generated by Django 2.2.5 on 2019-11-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_rating_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
