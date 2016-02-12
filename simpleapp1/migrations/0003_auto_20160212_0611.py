# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp1', '0002_auto_20160212_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='file',
            field=models.FileField(upload_to=b'files'),
        ),
    ]
