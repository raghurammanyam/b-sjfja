# Generated by Django 2.1.1 on 2018-09-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billpay', '0007_auto_20180914_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'paid'), ('n', 'not_paid')], default='n', max_length=1),
        ),
    ]