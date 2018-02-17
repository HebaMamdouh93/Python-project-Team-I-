# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0015_auto_20180217_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(default=datetime.datetime(2018, 2, 17, 9, 31, 49, 136106, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
