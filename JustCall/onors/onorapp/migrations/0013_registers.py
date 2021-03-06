# Generated by Django 2.1 on 2018-08-27 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onorapp', '0012_categories_show_in_mainpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('enquiry', models.TextField()),
                ('acknowledge', models.BooleanField(default=True)),
                ('status', models.CharField(max_length=100)),
                ('acknowledge_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onorapp.Users')),
            ],
        ),
    ]
