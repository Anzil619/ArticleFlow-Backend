# Generated by Django 5.0 on 2023-12-10 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_preferences'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Preferences',
        ),
    ]
