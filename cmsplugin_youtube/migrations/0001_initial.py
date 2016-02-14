# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('video_id', models.CharField(max_length=12)),
                ('autoplay', models.BooleanField(default=False)),
                ('hide_info', models.BooleanField(default=False, help_text="Don't display the title and uploader before the video starts.")),
                ('light_theme', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
