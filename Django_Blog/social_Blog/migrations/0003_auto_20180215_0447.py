# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0002_auto_20180214_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(to='social_Blog.Category'),
        ),
    ]
