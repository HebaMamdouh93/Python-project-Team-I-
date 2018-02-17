# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0014_auto_20180217_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(null=True, upload_to=b'ima', blank=True),
        ),
    ]
