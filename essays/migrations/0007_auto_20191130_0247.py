# Generated by Django 2.2.5 on 2019-11-30 02:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essays', '0006_auto_20191124_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=10000, validators=[django.core.validators.MinLengthValidator(150)]),
        ),
    ]
