# Generated by Django 2.1 on 2018-08-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.IntegerField(default=0)),
                ('amount', models.IntegerField()),
                ('change', models.IntegerField()),
                ('Rs2000', models.IntegerField()),
                ('Rs500', models.IntegerField()),
                ('Rs200', models.IntegerField()),
                ('Rs100', models.IntegerField()),
                ('Rs50', models.IntegerField()),
                ('Rs10', models.IntegerField()),
                ('Rs5', models.IntegerField()),
                ('Rs2', models.IntegerField()),
                ('Rs1', models.IntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rs2000', models.IntegerField(default=0)),
                ('Rs500', models.IntegerField(default=0)),
                ('Rs200', models.IntegerField(default=0)),
                ('Rs100', models.IntegerField(default=0)),
                ('Rs50', models.IntegerField(default=0)),
                ('Rs10', models.IntegerField(default=0)),
                ('Rs5', models.IntegerField(default=0)),
                ('Rs2', models.IntegerField(default=0)),
                ('Rs1', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
