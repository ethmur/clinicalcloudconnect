# Generated by Django 2.1.2 on 2018-10-07 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_hps'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvidesFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.HealthProvider')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='hps',
        ),
        migrations.AddField(
            model_name='providesfor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
