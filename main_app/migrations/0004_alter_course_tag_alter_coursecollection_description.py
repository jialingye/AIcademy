# Generated by Django 4.2.2 on 2023-07-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_delete_studentinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='coursecollection',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
