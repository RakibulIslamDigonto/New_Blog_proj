# Generated by Django 3.2.5 on 2021-07-28 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0006_auto_20210727_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Blog_app.blog')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
    ]
