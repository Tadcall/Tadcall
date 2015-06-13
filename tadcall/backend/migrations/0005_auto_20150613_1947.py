# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_locationrestriction_numbercallsrestriction_timerestriction'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationrestriction',
            name='link',
            field=models.ForeignKey(default=1, to='backend.Link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='numbercallsrestriction',
            name='link',
            field=models.ForeignKey(default=1, to='backend.Link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timerestriction',
            name='link',
            field=models.ForeignKey(default=1, to='backend.Link'),
            preserve_default=False,
        ),
    ]
