# Generated by Django 3.0.5 on 2020-04-15 21:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0003_auto_20200413_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDonated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=105)),
                ('serial_number', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('notes', models.TextField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='users',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
