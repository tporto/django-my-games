# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('publication_date', models.DateField(null=True)),
                ('developer', models.CharField(blank=True, max_length=155, null=True)),
                ('game_type', models.PositiveSmallIntegerField(choices=[(1, 'PS4'), (2, 'Xbox One'), (3, 'PC'), (4, 'Wii U'), (5, 'Mobile')])),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='images/')),
                ('cover', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Photo'),
        ),
    ]
