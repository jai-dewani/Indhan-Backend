# Generated by Django 2.2.4 on 2020-02-07 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20200207_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petrolpump',
            old_name='sanity',
            new_name='sanitation',
        ),
    ]