# Generated by Django 4.1 on 2022-08-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_caught_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='caught',
            options={'ordering': ['-date']},
        ),
    ]
