# Generated by Django 2.1.1 on 2018-09-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billpay', '0002_auto_20180914_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[(1, 'paid'), (2, 'not_paid')], default=1, max_length=1),
        ),
    ]