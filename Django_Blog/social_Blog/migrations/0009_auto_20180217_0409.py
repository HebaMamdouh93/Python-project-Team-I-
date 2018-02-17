# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0008_auto_20180217_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.CharField(max_length=255),
        ),
    ]
