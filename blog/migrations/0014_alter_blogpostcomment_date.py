# Generated by Django 4.0.5 on 2022-07-03 04:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_blogpostcomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcomment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 4, 42, 22, 365155, tzinfo=utc), verbose_name='Date'),
        ),
    ]
