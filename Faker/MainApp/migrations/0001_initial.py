# Generated by Django 2.1.1 on 2018-09-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('job', models.CharField(max_length=44)),
                ('email', models.CharField(max_length=55)),
            ],
        ),
    ]
