# Generated by Django 4.1.3 on 2022-11-13 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Estado',
            new_name='estado',
        ),
    ]