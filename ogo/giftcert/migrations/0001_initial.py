# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(help_text='Enter the full name of the person whose account you would like us to credit. They must be an OGO member in good standing.', max_length=256)),
                ('from_name', models.CharField(max_length=256, verbose_name='From')),
                ('from_email', models.EmailField(max_length=256)),
                ('from_phone', models.CharField(blank=True, max_length=32)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('staff_notes', models.TextField(blank=True)),
                ('paid', models.BooleanField(default=False)),
                ('applied_to_account', models.BooleanField(default=False)),
                ('confirmation_sent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-order_date',),
            },
        ),
    ]
