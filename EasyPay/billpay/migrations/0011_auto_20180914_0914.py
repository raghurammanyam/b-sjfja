# Generated by Django 2.1.1 on 2018-09-14 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billpay', '0010_auto_20180914_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='billpay.users'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='pay_status',
            field=models.BooleanField(default=True),
        ),
    ]