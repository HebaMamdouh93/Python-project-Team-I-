# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(related_name='category', to='social_Blog.Category'),
        ),
    ]
