# Generated by Django 4.0.3 on 2022-04-26 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='update',
            new_name='updated_at',
        ),
    ]
