# Generated by Django 3.0.5 on 2020-04-26 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='address',
        ),
    ]
