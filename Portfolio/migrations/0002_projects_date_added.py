# Generated by Django 5.0 on 2024-04-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]
