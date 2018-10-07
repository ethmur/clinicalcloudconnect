# Generated by Django 2.1.2 on 2018-10-07 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprovider',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='healthprovider',
            name='tele',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='current_medications',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='employer',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='health_provider',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='medical_conditions',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='tele',
            field=models.TextField(default='', max_length=100),
        ),
    ]
