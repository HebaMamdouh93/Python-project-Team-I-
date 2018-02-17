# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0004_auto_20180216_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='date',
        ),
    ]
