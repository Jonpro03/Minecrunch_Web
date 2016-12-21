# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modpacks', '0003_modpack_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Server Name')),
                ('desc', models.TextField(blank=True, verbose_name='Server Description')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Server Address')),
                ('screenshot', models.ImageField(blank=True, upload_to=b'', verbose_name='Screenshot')),
                ('dynmap', models.CharField(blank=True, max_length=200, verbose_name='DynMap URL')),
                ('slug', models.SlugField()),
                ('modpack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modpacks.Modpack', verbose_name='Server Modpack')),
            ],
        ),
    ]