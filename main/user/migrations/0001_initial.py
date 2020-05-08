# Generated by Django 3.0.6 on 2020-05-08 12:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('profile_pic', models.CharField(blank=True, max_length=255)),
                ('searchhistory', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=list, max_length=140), size=None)),
            ],
        ),
    ]