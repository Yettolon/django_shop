# Generated by Django 3.2 on 2022-03-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_product_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='address',
            field=models.CharField(default=None, max_length=100, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='Name'),
        ),
    ]