# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0012_auto_20180217_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
