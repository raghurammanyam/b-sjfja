# Generated by Django 2.1 on 2018-08-27 09:59

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=mainapp.models.sport_file_name),
        ),
    ]