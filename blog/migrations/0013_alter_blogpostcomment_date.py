# Generated by Django 4.0.5 on 2022-07-03 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blogpostcomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcomment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]
