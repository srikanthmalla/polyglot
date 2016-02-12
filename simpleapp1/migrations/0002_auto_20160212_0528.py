# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='file',
            field=models.FileField(upload_to=b'chacha.jpeg'),
        ),
    ]
