# Generated by Django 4.1 on 2022-08-04 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='description',
            new_name='scientific_name',
        ),
    ]