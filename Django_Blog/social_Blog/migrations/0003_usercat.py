# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_Blog', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat', models.ForeignKey(to='social_Blog.Category')),
                ('user', models.ForeignKey(to='social_Blog.User')),
            ],
        ),
    ]
