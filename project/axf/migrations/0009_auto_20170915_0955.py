# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 01:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0008_cart_orderid'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cart',
            managers=[
                ('object1', django.db.models.manager.Manager()),
            ],
        ),
    ]
