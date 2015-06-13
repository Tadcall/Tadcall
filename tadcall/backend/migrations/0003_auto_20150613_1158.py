# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='link',
            name='real_phone_number',
            field=models.ForeignKey(default='1', to='backend.RealPhoneNumber'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='virtual_phone_number',
            field=models.ForeignKey(default='1', to='backend.VirtualPhoneNumber'),
            preserve_default=False,
        ),
    ]
