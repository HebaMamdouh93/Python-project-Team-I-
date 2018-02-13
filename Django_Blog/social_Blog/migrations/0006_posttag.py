# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0005_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.ForeignKey(to='social_Blog.Post')),
                ('tag', models.ForeignKey(to='social_Blog.Tag')),
            ],
        ),
    ]
