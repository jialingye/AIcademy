# Generated by Django 4.2.2 on 2023-07-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='score',
            name='input',
            field=models.TextField(default=''),
        ),
    ]
