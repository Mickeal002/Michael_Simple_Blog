# Generated by Django 4.0.5 on 2022-07-23 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('body', models.CharField(max_length=12000000)),
                ('uploaded_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
