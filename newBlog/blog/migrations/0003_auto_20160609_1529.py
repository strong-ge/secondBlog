# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='top',
            field=models.BooleanField(default=b'false'),
        ),
        migrations.AlterField(
            model_name='image',
            name='blog',
            field=models.ForeignKey(related_name='get_image', to='blog.Blog'),
        ),
    ]
