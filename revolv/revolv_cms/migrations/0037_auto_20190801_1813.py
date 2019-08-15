# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('revolv_cms', '0036_auto_20160204_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginpagesettings',
            name='login_paragraph',
            field=wagtail.wagtailcore.fields.RichTextField(default=b"<p>Log in to see the impact you're having, bringing solar energy to communities around the country. </p>", help_text=b'The paragraph of text to be shown under the heading on the login page, but before the links to the register page and the forgot password page.', blank=True),
            preserve_default=True,
        ),
    ]
