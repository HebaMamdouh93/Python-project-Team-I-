# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0007_auto_20180217_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(upload_to=b'images/'),
        ),
    ]
