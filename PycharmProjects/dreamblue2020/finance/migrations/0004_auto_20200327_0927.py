# Generated by Django 3.0.4 on 2020-03-27 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20200327_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leasespace',
            old_name='notes',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='tenant',
            old_name='notes',
            new_name='note',
        ),
    ]
