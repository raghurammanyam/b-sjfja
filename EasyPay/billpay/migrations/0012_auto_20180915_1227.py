# Generated by Django 2.1.1 on 2018-09-15 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billpay', '0011_auto_20180914_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='transaction',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='billpay.transactions'),
        ),
    ]