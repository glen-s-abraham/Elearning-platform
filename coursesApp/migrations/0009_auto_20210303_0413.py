# Generated by Django 3.1.1 on 2021-03-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0008_auto_20201003_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cover',
            field=models.FileField(null=True, upload_to='Courses/'),
        ),
    ]