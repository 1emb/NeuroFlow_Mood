# Generated by Django 3.0.8 on 2020-07-24 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_usermood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermood',
            old_name='name',
            new_name='username',
        ),
    ]
