# Generated by Django 3.2.5 on 2021-07-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carousel_app', '0004_auto_20210725_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog_thumbnail', models.ImageField(upload_to='blogs_image/')),
                ('discription', models.TextField()),
            ],
        ),
    ]
