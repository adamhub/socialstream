# Generated by Django 3.2.2 on 2021-05-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsite', '0008_auto_20210519_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='cat',
            field=models.IntegerField(choices=[(0, 'Standard Page'), (1, 'Video Post Page'), (2, 'Image Post Page'), (3, 'News Post Page')], default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Blog Pgae Header Image'),
        ),
    ]
