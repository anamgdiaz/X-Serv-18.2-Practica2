# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20180407_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls_mod',
            old_name='url',
            new_name='url_long',
        ),
    ]
