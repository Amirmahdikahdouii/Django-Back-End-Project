# Generated by Django 4.0.5 on 2022-07-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='blog_writer',
            field=models.BooleanField(default=False, verbose_name='Blog Writer'),
        ),
    ]
