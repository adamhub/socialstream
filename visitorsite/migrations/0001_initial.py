# Generated by Django 3.2.2 on 2021-05-12 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Page Title')),
                ('slug', models.CharField(max_length=250, verbose_name="Page's URL Slug'")),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='visitorsite.page')),
            ],
            bases=('visitorsite.page',),
        ),
    ]
