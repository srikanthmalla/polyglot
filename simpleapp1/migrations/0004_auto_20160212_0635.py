# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import simpleapp1.models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp1', '0003_auto_20160212_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='file',
            field=models.FileField(upload_to=simpleapp1.models.generate_filename),
        ),
    ]
