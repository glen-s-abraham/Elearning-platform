# Generated by Django 3.1.7 on 2021-03-05 03:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=500)),
                ('course', models.CharField(choices=[('BSC.CS', 'Bsc computerScience'), ('MSC.CS', 'Msc computerScience')], default='BSC.CS', max_length=20)),
                ('semester', models.CharField(choices=[('S1', 'semester 1'), ('S2', 'semester 2'), ('S3', 'semester 3'), ('S4', 'semester 4'), ('S5', 'semester 5'), ('S6', 'semester 6')], default='S1', max_length=3)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]