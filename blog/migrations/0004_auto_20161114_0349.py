# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_tag_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', to_field='name', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='分类名称'),
        ),
    ]
