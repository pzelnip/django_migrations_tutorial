# Generated by Django 3.2.20 on 2023-09-11 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_migrations_tutorial', '0002_zapp_zdl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zapp',
            old_name='zdl',
            new_name='zap_definition_language',
        ),
    ]
