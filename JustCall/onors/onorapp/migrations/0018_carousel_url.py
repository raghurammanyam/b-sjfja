# Generated by Django 2.1 on 2018-08-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onorapp', '0017_auto_20180828_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
