# Generated by Django 4.0.5 on 2022-06-27 17:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpostcomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 27, 17, 42, 59, 152189, tzinfo=utc), verbose_name='Date'),
        ),
    ]
