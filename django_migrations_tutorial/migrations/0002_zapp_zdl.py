# Generated by Django 3.2.20 on 2023-09-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_migrations_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapp',
            name='zdl',
            field=models.JSONField(default=dict),
        ),
    ]
