# Generated by Django 2.0.7 on 2018-07-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopItems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='mobile_no',
            field=models.CharField(max_length=20),
        ),
    ]