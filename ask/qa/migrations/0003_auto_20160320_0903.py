# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20160317_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
