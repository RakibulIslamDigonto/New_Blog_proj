# Generated by Django 3.2.5 on 2021-07-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0002_auto_20210727_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
