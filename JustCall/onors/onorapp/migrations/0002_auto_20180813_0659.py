# Generated by Django 2.1 on 2018-08-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onorapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='emailId',
            field=models.EmailField(blank=True, default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
