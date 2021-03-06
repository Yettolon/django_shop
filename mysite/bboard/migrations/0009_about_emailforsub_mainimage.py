# Generated by Django 3.2 on 2022-03-19 16:07

import bboard.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0008_auto_20220318_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='It`s text', verbose_name='Text')),
                ('addres', models.CharField(blank=True, default=None, max_length=60, verbose_name='Address')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Email')),
                ('mmm', models.BooleanField(default=False, verbose_name='in?')),
            ],
        ),
        migrations.CreateModel(
            name='EmailForSub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emaill', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('content', models.CharField(max_length=60, verbose_name='Content')),
                ('image', models.ImageField(upload_to=bboard.utilities.timestapppp, verbose_name='Image')),
                ('in_jobs', models.BooleanField(default=True, verbose_name='In jobs?')),
                ('order', models.SmallIntegerField(db_index=True, default=0, unique=True, verbose_name='int sort')),
            ],
            options={
                'verbose_name': 'MainImage',
                'verbose_name_plural': 'MainImage',
            },
        ),
    ]
