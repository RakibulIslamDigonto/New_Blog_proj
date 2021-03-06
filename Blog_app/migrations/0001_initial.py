# Generated by Django 3.2 on 2021-07-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blog_thumbnail', models.ImageField(upload_to='blog_img/')),
                ('short_discription', models.CharField(max_length=500)),
                ('discription', models.TextField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
