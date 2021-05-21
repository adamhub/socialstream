# Generated by Django 3.2.2 on 2021-05-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsite', '0009_auto_20210519_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='cat',
        ),
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.IntegerField(choices=[(0, 'Standard Page'), (1, 'Video Post Page'), (2, 'Image Post Page'), (3, 'News Post Page')], default=0),
        ),
    ]
