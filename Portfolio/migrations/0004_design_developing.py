# Generated by Django 5.0 on 2024-04-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_projects_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Design',
                'verbose_name_plural': 'Designing',
            },
        ),
        migrations.CreateModel(
            name='Developing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Developing',
                'verbose_name_plural': 'Developing',
            },
        ),
    ]
