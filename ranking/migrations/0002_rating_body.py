# Generated by Django 2.2.5 on 2019-11-27 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='body',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
