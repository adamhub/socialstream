# Generated by Django 3.2.2 on 2021-07-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccomment',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name="user's email address"),
        ),
    ]
